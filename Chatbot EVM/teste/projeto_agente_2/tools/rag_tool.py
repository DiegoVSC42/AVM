from typing import List
import os

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document

from config import (
    LLM_MODEL,
    EMBED_MODEL,
    RAG_SYSTEM,
    RAG_HUMAN,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    RETRIEVER_K,
    INDICES_DIR,
    WHATSAPP_MODE,
    MAX_LINES,
    MAX_CHARS_PER_LINE,
    SHOW_SOURCES,
)


def _carregar_documento(caminho: str) -> List[Document]:
    caminho_lower = caminho.lower()
    if caminho_lower.endswith(".pdf"):
        loader = PyPDFLoader(caminho)
    else:
        loader = TextLoader(caminho, encoding="utf-8")
    return loader.load()


def _construir_vetores(doc_path: str) -> FAISS:
    docs = _carregar_documento(doc_path)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    chunks = splitter.split_documents(docs)
    embeddings = OllamaEmbeddings(model=EMBED_MODEL)
    vectordb = FAISS.from_documents(chunks, embeddings)
    return vectordb


def carregar_ou_construir_indice(name: str, path: str, persist: bool) -> FAISS:
    embeddings = OllamaEmbeddings(model=EMBED_MODEL)
    indice_dir = os.path.join(INDICES_DIR, name)

    if persist and os.path.isdir(indice_dir):
        try:
            vectordb = FAISS.load_local(
                indice_dir,
                embeddings,
                allow_dangerous_deserialization=True,
            )
            return vectordb
        except Exception:
            pass

    vectordb = _construir_vetores(path)
    if persist:
        os.makedirs(indice_dir, exist_ok=True)
        vectordb.save_local(indice_dir)
    return vectordb


def _soft_wrap(texto: str, max_chars: int) -> str:
    linhas = []
    for raw_line in texto.splitlines():
        line = " ".join(raw_line.strip().split())
        while len(line) > max_chars:
            # quebra "suave" na última posição de espaço antes do limite
            cut = line.rfind(" ", 0, max_chars)
            cut = cut if cut != -1 else max_chars
            linhas.append(line[:cut].rstrip())
            line = line[cut:].lstrip()
        if line:
            linhas.append(line)
    return "\n".join(linhas)


def _to_bullets(texto: str) -> str:
    # transforma em bullets simples (no máximo MAX_LINES)
    parts = [p.strip("-• ").strip() for p in texto.split("\n") if p.strip()]
    if not parts:
        return ""
    # pega até MAX_LINES itens
    parts = parts[:MAX_LINES]
    return "\n".join(f"• {p}" for p in parts)


def _whatsappify(texto: str) -> str:
    """Simplifica e formata o texto para parecer conversa de WhatsApp."""
    if not WHATSAPP_MODE:
        return texto.strip()

    # remove marcações
    texto = texto.replace("**", "").replace("__", "").strip()

    # quebra em sentenças pelo ponto final
    partes = [p.strip() for p in texto.split(".") if p.strip()]

    # transforma cada sentença em bullet
    bullets = [f"• {p}" for p in partes]

    # pega até MAX_LINES bullets
    bullets = bullets[:MAX_LINES]

    return "\n".join(bullets)


class FerramentaRAG:
    """Tool única por documento, realiza RAG usando FAISS + Ollama."""

    def __init__(self, vectordb: FAISS, model_name: str = LLM_MODEL):
        self.retriever = vectordb.as_retriever(
            search_type="similarity",
            search_kwargs={"k": RETRIEVER_K},
        )
        self.llm = ChatOllama(model=model_name, temperature=0.2)
        self.prompt = ChatPromptTemplate.from_messages(
            [("system", RAG_SYSTEM), ("human", RAG_HUMAN)]
        )

    def __call__(self, pergunta: str) -> str:
        docs = self.retriever.invoke(pergunta)
        if not docs:
            return _whatsappify(
                "Não achei essa informação no material. Posso te ajudar de outro jeito?"
            )

        contexto = "\n\n---\n\n".join(d.page_content for d in docs)
        messages = self.prompt.format_messages(pergunta=pergunta, contexto=contexto)
        resposta_msg = self.llm.invoke(messages)
        resposta = getattr(resposta_msg, "content", str(resposta_msg)).strip()

        # fontes (limitadas pra não virar textão)
        if SHOW_SOURCES > 0:
            fontes = []
            for d in docs:
                meta = d.metadata or {}
                page = meta.get("page")
                origem = meta.get("source", "")
                if page is not None:
                    fontes.append(f"{origem} (pág. {page + 1})")
                else:
                    fontes.append(origem or "fonte desconhecida")
            fontes_unicas = [f for f in dict.fromkeys(fontes) if f][:SHOW_SOURCES]
        else:
            fontes_unicas = []

        resposta = _whatsappify(resposta)

        if fontes_unicas:
            # acrescenta 1 linha curta de fonte
            resposta += f"\n\n🔎 Fonte: {', '.join(fontes_unicas)}"
        return resposta
