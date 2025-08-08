from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

modelo = ChatOllama(
    model="mistral",
    temperature=0.5,
)

prompt_sugestao = ChatPromptTemplate.from_messages(
    [
        ("system", "Você é um guia de viagem especializado em destinos brasileiros"),
        ("placeholder", "{historico}"),
        ("human", "{query}"),
    ]
)

cadeia = prompt_sugestao | modelo | StrOutputParser()

memoria = {}
sessao = "aula_langchain"


def historico_por_sessao(sessao: str):
    if sessao not in memoria:
        memoria[sessao] = InMemoryChatMessageHistory()
    return memoria[sessao]


perguntas = [
    "Quero visitar um lugar no Brasil, famoso por praias e cultura. Pode sugerir ?",
    "Qual a melhor época do ano para ir ?",
]

cadeia_com_memoria = RunnableWithMessageHistory(
    runnable=cadeia,
    get_session_history=historico_por_sessao,
    input_messages_key="query",
    history_messages_key="historico",
)

for pergunta in perguntas:
    resposta = cadeia_com_memoria.invoke(
        {"query": pergunta},
        config={"session_id": sessao},
    )
    print("Usuário: ", pergunta)
    print("IA:      ", resposta)
    print("\n")
