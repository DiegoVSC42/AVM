
import os
import chainlit as cl
from config import llm
from prompts import criar_prompt_rag
from pdf_loader import carregar_pdf, juntar_conteudo

# Carregar TODOS os PDFs da pasta documentos
docs = []
documentos_dir = os.path.join(os.path.dirname(__file__), "documentos")

for arquivo in os.listdir(documentos_dir):
    if arquivo.lower().endswith(".pdf"):
        caminho = os.path.join(documentos_dir, arquivo)
        docs.extend(carregar_pdf(caminho))

# Criar contexto único a partir de todos os PDFs
contexto = juntar_conteudo(docs)

@cl.on_chat_start
async def start():
    await cl.Message(
        content="🤖 Olá! Pode me fazer perguntas sobre os documentos carregados."
    ).send()

@cl.on_message
async def main(message: cl.Message):
    pergunta = message.content

    prompt_rag = criar_prompt_rag()
    chain_rag = prompt_rag | llm
    resposta = chain_rag.invoke({"contexto": contexto, "pergunta": pergunta})

    await cl.Message(content=str(resposta.content)).send()
