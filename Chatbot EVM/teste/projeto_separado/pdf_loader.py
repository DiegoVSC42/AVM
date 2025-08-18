
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def carregar_pdf(caminho_pdf: str):
    loader = PyPDFLoader(caminho_pdf)
    docs = loader.load()
    return docs

def juntar_conteudo(docs):
    return "\n".join(doc.page_content for doc in docs)

def dividir_em_chunks(docs, chunk_size=800, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(docs)
