from agent import AgenteMultiRAG


def main():
    agente = AgenteMultiRAG()
    agente.carregar_tools()

    print("Oi! 👋 Atendimento do Eu Vereador Mandato.")
    print("Comandos: :tools | :use NOME | @NOME pergunta | sair\n")
    print(agente.listar_tools())

    while True:
        try:
            entrada = input("Você: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nAté mais! 🙂")
            break

        if not entrada:
            continue
        if entrada.lower() in {"sair", "exit", "quit"}:
            print("Até mais! 🙂")
            break

        resposta = agente.responder(entrada)
        print("\nAgente:\n" + resposta + "\n")


if __name__ == "__main__":
    main()
