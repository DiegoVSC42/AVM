from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

llm = ChatOllama(
    model="mistral",
    temperature=0.3,  # mais “obediente” para seguir ferramenta
)

model_name = "sentence-transformers/all-mpnet-base-v2"
embed_model = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True},  # <- normalize = True
)


def ingest(document: str):
    # Get the doc
    loader = PyPDFLoader(document)
    pages = loader.load_and_split()
    # Split the pages by char
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1024,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(pages)
    print(f"Split {len(pages)} documents into {len(chunks)} chunks.")
    #
    embedding = FastEmbedEmbeddings()
    # Create vector store
    Chroma.from_documents(
        documents=chunks, embedding=embedding, persist_directory="./sql_chroma_db"
    )
