from langchain_ollama import ChatOllama
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate

# 1. LLM do Ollama
modelo = ChatOllama(model="mistral", temperature=0.5)

# 2. Embeddings gratuitos via HuggingFace
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 3. Carregar documento
arquivos = [
    r"LangChain\Curso 1\documentos\GTB_standard_Nov23.pdf",
    r"LangChain\Curso 1\documentos\GTB_gold_Nov23.pdf",
    r"LangChain\Curso 1\documentos\GTB_platinum_Nov23.pdf",
]


documentos = sum([PyPDFLoader(arquivo).load() for arquivo in arquivos], [])


# 4. Split em pedaços
pedacos = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
).split_documents(documentos)

# 5. FAISS index + retriever
dados_recuperados = FAISS.from_documents(pedacos, embeddings).as_retriever(
    search_kwargs={"k": 2}
)

# 6. Prompt
prompt_consulta_seguro = ChatPromptTemplate.from_messages(
    [
        ("system", "Responda usando exclusivamente o conteudo fornecido"),
        ("human", "{query}\n\nContexto: \n{contexto}\n\nResposta:"),
    ]
)

# 7. Cadeia de execução
cadeia = prompt_consulta_seguro | modelo | StrOutputParser()


# 8. Função de resposta
def responder(pergunta: str):
    trechos = dados_recuperados.invoke(pergunta)
    contexto = "\n\n".join(um_trecho.page_content for um_trecho in trechos)
    return cadeia.invoke({"query": pergunta, "contexto": contexto})


print(
    responder(
        "Como devo proceder caso tenha um item roubado e caso eu tenha um cartao platinum?"
    )
)
