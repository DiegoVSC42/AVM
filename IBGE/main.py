import warnings
from langchain_core._api.deprecation import LangChainDeprecationWarning

warnings.filterwarnings("ignore", category=LangChainDeprecationWarning)

from agente import AgenteOllama

if __name__ == "__main__":
    agente = AgenteOllama()
    print("\nAgente pronto. Faça sua pergunta:")

    pergunta_usuario = "Quantos habitantes tem em formosa ?"

    # Adiciona instrução para manter o idioma
    pergunta = f"Responda no mesmo idioma da pergunta original: {pergunta_usuario}"
    print("\nPergunta formatada:", pergunta)

    resposta = agente.perguntar(pergunta)
    print("\nResposta:", resposta)
