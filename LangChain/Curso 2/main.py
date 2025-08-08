import warnings
from langchain_core._api.deprecation import LangChainDeprecationWarning

warnings.filterwarnings("ignore", category=LangChainDeprecationWarning)

from agente import AgenteOllama

if __name__ == "__main__":
    agente = AgenteOllama()
    print("Agente pronto. Faça sua pergunta:")

    pergunta_usuario = "Quais as faculdades com melhores chances para ana entrar ?"

    # Adiciona instrução para manter o idioma
    pergunta = f"Responda no mesmo idioma da pergunta original: {pergunta_usuario}"
    print("Pergunta formatada:", pergunta)

    resposta = agente.perguntar(pergunta)
    print("Resposta:", resposta)
