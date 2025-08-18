# app.py (trecho principal)
import chainlit as cl
from rag_chain_clara import rag_chain_clara

chain = rag_chain_clara()


@cl.on_chat_start
async def start():
    await cl.Message(
        content="👋 Olá! Eu é a Clara. Pergunte sobre Comunicação Estratégica de Mandato!"
    ).send()


@cl.on_message
async def main(message: cl.Message):
    pergunta = message.content
    # a retrieval_chain retorna dict com "answer" e "context"
    resp = await cl.make_async(chain.invoke)({"input": pergunta})
    texto = resp.get("answer", "Não encontrei essa informação no material do curso.")
    await cl.Message(content=texto).send()
