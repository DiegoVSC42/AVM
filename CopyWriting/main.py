from agente import AgenteOllama
from ferramenta_carta_proposta import DadosCartaProposta
from langchain.agents import Tool

if __name__ == "__main__":
    docx_path = r"CopyWriting\documentos\Carta Proposta - Eu Vereador Mandato.docx"
    ferramenta_carta = DadosCartaProposta(path=docx_path)

    tools = [
        Tool(
            name=ferramenta_carta.name,
            func=ferramenta_carta.run,
            description=ferramenta_carta.description,
        )
    ]

    agente = AgenteOllama(tools)
    print("\nAgente pronto!")

    while True:
        pergunta = input("\nDigite sua pergunta (ou 'sair' para encerrar): ")
        if pergunta.strip().lower() == "sair":
            print("Saindo... Até mais!")
            break
        resposta = agente.perguntar(pergunta)
        print("\nResposta:", resposta)
