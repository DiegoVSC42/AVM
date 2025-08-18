from langchain.prompts import ChatPromptTemplate
import os


def criar_prompt_rag():
    # Caminho para o arquivo de prompt
    caminho_txt = os.path.join(os.path.dirname(__file__), "prompts", "prompt_base.txt")

    # Ler o conteúdo do arquivo
    with open(caminho_txt, "r", encoding="utf-8") as f:
        template_texto = f.read()

    # Criar e retornar o prompt
    return ChatPromptTemplate.from_template(template_texto)
