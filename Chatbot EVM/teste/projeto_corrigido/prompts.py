
from langchain.prompts import ChatPromptTemplate

def criar_prompt_rag():
    return ChatPromptTemplate.from_template(
        """
Use o contexto abaixo para responder a pergunta.
Se não souber a resposta baseado no contexto, diga que não tem a informação.

Contexto: {contexto}

Pergunta: {pergunta}"""
    )
