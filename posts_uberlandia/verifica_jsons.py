import json
from collections import defaultdict

ids_encontrados = defaultdict(list)

for i in range(1, 29):
    arquivo = f"{i}.json"

    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
    except FileNotFoundError:
        print(f"[AVISO] Arquivo {arquivo} não encontrado")
        continue

    if not isinstance(dados, list):
        print(f"[ERRO] {arquivo} não é uma lista")
        continue

    for item in dados:
        if "id" in item:
            ids_encontrados[item["id"]].append(arquivo)

# Verificando duplicados
repetidos = {k: v for k, v in ids_encontrados.items() if len(v) > 1}

if repetidos:
    print("❌ IDs repetidos encontrados:")
    for id_, arquivos in repetidos.items():
        print(f"ID {id_} aparece em: {', '.join(arquivos)}")
else:
    print("✅ Nenhum ID repetido encontrado")
