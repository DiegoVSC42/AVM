
# Ponto de entrada: aqui você fará as perguntas.
# Ele carrega o índice (Chroma), cria o ensemble retriever e chama a cadeia de chat com a LLM do Ollama (mistral).

from retrieval import load_vector_retriever, make_ensemble_retriever
from chain import build_chain

def banner():
    print("""
==============================================
 Assistente RAG (Ollama — mistral)  —  Pergunte!
 Digite 'sair' para encerrar.
==============================================
""")

def main():
    banner()
    print("Carregando retriever...")
    vs = load_vector_retriever()
    retriever = make_ensemble_retriever(vs)
    chat_fn = build_chain(retriever)

    history = []  # [(human, ai), ...]

    while True:
        try:
            q = input("Você: ").strip()
        except EOFError:
            break
        if not q:
            continue
        if q.lower() in {"sair", "exit", "quit"}:
            print("Até logo!")
            break

        try:
            answer = chat_fn({"question": q, "history": history})
            print("\nAssistente:\n" + answer + "\n")
            history.append((q, answer))
        except Exception as e:
            print("Ocorreu um erro:", e)

if __name__ == "__main__":
    main()
