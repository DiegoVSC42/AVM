
from typing import List, Dict
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.messages import AIMessage, HumanMessage
from langchain.memory import ConversationBufferWindowMemory

from config import OLLAMA_LLM_MODEL, MEMORY_WINDOW
from utils import pretty_sources

SYSTEM_PROMPT = """
Você é um assistente especialista em responder com base APENAS nos documentos fornecidos no contexto.
Se a resposta não estiver nos documentos, explique de forma simples que não encontrou a informação nos materiais.
Seja claro, objetivo e cordial.
"""

def build_chain(retriever):
    llm = ChatOllama(model=OLLAMA_LLM_MODEL, temperature=0.2)

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "Pergunta: {question}\n\nContexto:\n{context}\n\nResponda de forma direta e cite as fontes quando possível."),
    ])

    def format_docs(docs: List) -> str:
        chunks = []
        sources = []
        for d in docs:
            src = d.metadata.get("source", d.metadata.get("source_file", "desconhecido"))
            sources.append(src)
            chunks.append(f"[Fonte: {src}]\n{d.page_content}")
        return "\n\n".join(chunks), list(dict.fromkeys(sources))  # mantém ordem, remove duplicadas

    memory = ConversationBufferWindowMemory(k=MEMORY_WINDOW, return_messages=True)
    parser = StrOutputParser()

    # Pipeline: recuperação → formatação → LLM
    def _call(inputs: Dict):
        question = inputs.get("question", "")
        history = inputs.get("history", [])  # lista de (humano, ai)

        # Carrega histórico na memória
        memory.clear()
        for h, a in history[-MEMORY_WINDOW:]:
            memory.chat_memory.add_user_message(h)
            memory.chat_memory.add_ai_message(a)

        docs = retriever.get_relevant_documents(question)
        context_str, srcs = format_docs(docs)

        chain = prompt | llm | parser
        answer = chain.invoke({
            "chat_history": memory.load_memory_variables({})["history"],
            "question": question,
            "context": context_str
        })

        if srcs:
            answer += "\n\nFontes:\n" + pretty_sources(srcs)
        return answer

    return _call
