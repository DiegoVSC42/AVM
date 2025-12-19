import os
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

from config import DOCS_DIR, CHROMA_DIR, CHUNK_SIZE, CHUNK_OVERLAP, OLLAMA_EMBED_MODEL
from utils import clean_text


def load_pdfs_from_dir(dir_path: str):
    dirp = Path(dir_path)
    dirp.mkdir(parents=True, exist_ok=True)
    pdf_files = sorted([p for p in dirp.glob("*.pdf")])
    docs = []
    for pdf in pdf_files:
        loader = PyPDFLoader(str(pdf))
        pages = loader.load()
        for d in pages:
            d.page_content = clean_text(d.page_content)
            d.metadata = d.metadata or {}
            d.metadata["source_file"] = str(pdf.name)
        docs.extend(pages)
    return docs


def split_docs(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", " ", ""],
    )
    return splitter.split_documents(docs)


def build_vectorstore(chunks):
    embeddings = OllamaEmbeddings(model=OLLAMA_EMBED_MODEL)
    vs = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR,
    )

    return vs


def main():
    print(f"Carregando PDFs de: {DOCS_DIR}")
    docs = load_pdfs_from_dir(DOCS_DIR)
    if not docs:
        print(
            "Nenhum PDF encontrado. Coloque arquivos em 'documentos_curso/' e rode novamente."
        )
        return
    print(f"Total de páginas: {len(docs)}")
    chunks = split_docs(docs)
    print(f"Total de chunks: {len(chunks)}")

    print("Criando/atualizando o índice vetorial (Chroma)...")
    _ = build_vectorstore(chunks)
    print("✅ Banco vetorial criado/atualizado com sucesso em:", CHROMA_DIR)
    if chunks:
        print("Exemplo de metadados do primeiro chunk:", chunks[0].metadata)


if __name__ == "__main__":
    main()
