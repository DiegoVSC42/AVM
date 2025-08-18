from langchain_core.vectorstores import InMemoryVectorStore
from config import embed_model
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def carrega_pdf(url: str):
    loader = PyPDFLoader(url)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800, chunk_overlap=120, separators=["\n\n", "\n", ". ", " "]
    )
    chunks = splitter.split_documents(docs)
    vectorstore = InMemoryVectorStore.from_documents(chunks, embed_model)
    return vectorstore


vector_store_comunicacao = carrega_pdf("docs/Comunicacao_Mandato_Vereadores.pdf")
