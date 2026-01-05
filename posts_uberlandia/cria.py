import json

vetor = list(range(5, 29))

for x in vetor:
    nome_arquivo = f"{x}.json"
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump({}, f, ensure_ascii=False, indent=2)
