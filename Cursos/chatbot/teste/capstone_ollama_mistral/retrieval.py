
from typing import List, Optional, Union
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_community.retrievers import BM25Retriever
from langchain.schema import Document
from langchain_core.retrievers import BaseRetriever
from langchain.retrievers import EnsembleRetriever

from config import CHROMA_DIR, OLLAMA_EMBED_MODEL, TOP_K_VECTOR, TOP_K_BM25, ALPHA_ENSEMBLE

def load_vector_retriever() -> Chroma:
    embeddings = OllamaEmbeddings(model=OLLAMA_EMBED_MODEL)
    vs = Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)
    return vs

def _collect_docs_for_bm25(vs: Chroma) -> List[Document]:
    # Pega todos os documentos do Chroma. Limit alto para bases pequenas/médias.
    try:
        res = vs.get(include=["documents", "metadatas"], where={}, limit=100000)
        docs_raw = res.get("documents", []) or []
        metas_raw = res.get("metadatas", []) or []
        docs: List[Document] = []
        for txt, meta in zip(docs_raw, metas_raw):
            if txt and isinstance(txt, str):
                docs.append(Document(page_content=txt, metadata=meta or {}))
        return docs
    except Exception:
        # Se algo der errado (ex: base vazia), retorne lista vazia
        return []

def build_bm25_retriever_from_vs(vs: Chroma) -> Optional[BM25Retriever]:
    docs = _collect_docs_for_bm25(vs)
    if not docs:
        return None
    bm25 = BM25Retriever.from_documents(docs)
    bm25.k = TOP_K_BM25
    return bm25

def make_ensemble_retriever(vs: Chroma) -> BaseRetriever:
    vector_retriever = vs.as_retriever(search_kwargs={"k": TOP_K_VECTOR})
    bm25 = build_bm25_retriever_from_vs(vs)

    if bm25 is None:
        # Sem BM25 (base vazia ou erro), volta só o vetorial
        return vector_retriever

    # Combina os dois
    ensemble = EnsembleRetriever(
        retrievers=[vector_retriever, bm25],
        weights=[ALPHA_ENSEMBLE, 1 - ALPHA_ENSEMBLE],
    )
    return ensemble
