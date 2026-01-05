import json

todos = []

for i in range(1, 29):
    arquivo = f"{i}.json"

    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
    except FileNotFoundError:
        print(f"[AVISO] {arquivo} não encontrado, pulando...")
        continue

    if not isinstance(dados, list):
        print(f"[ERRO] {arquivo} não é uma lista, pulando...")
        continue

    todos.extend(dados)

with open("todos.json", "w", encoding="utf-8") as f:
    json.dump(todos, f, ensure_ascii=False, indent=2)

print(f"✅ Arquivo 'todos.json' criado com {len(todos)} registros")
