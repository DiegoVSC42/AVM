import os

# ================= CONFIG GERAL =================
LLM_MODEL = "mistral"
EMBED_MODEL = "nomic-embed-text"

RAG_SYSTEM = """
Você é uma atendente de WhatsApp que conversa com vereadores de todas as regiões do Brasil
sobre o curso 'Eu Vereador Mandato'.

Fale sempre de forma simples, clara e acolhedora, lembrando que muitos vereadores não têm formação acadêmica
e preferem explicações diretas e fáceis de entender.

Se não encontrar a resposta no documento fornecido, diga de maneira educada e sensível que não encontrou,
sem inventar informações.

Seu objetivo é ajudar o vereador a compreender o conteúdo do curso com respeito, proximidade e linguagem acessível.
"""

RAG_HUMAN = """
Pergunta: {pergunta}

Contexto:
{contexto}

Responda em até 4 linhas, frases curtas, linguagem simples.
Se necessário, ofereça ajuda prática com 1 passo seguinte.
Evite parágrafos longos.
"""

# --- adicione estes controles de "tom WhatsApp" ---
WHATSAPP_MODE = True
MAX_LINES = 5  # máx. de linhas por resposta
MAX_CHARS_PER_LINE = 0  # máx. de caracteres por linha
SHOW_SOURCES = 0  # quantas fontes mostrar no final (0 = ocultar)

# ================= DOCUMENTOS / TOOLS =================
# Cada item vira uma tool de RAG
DOCS = [
    {
        "name": "comunicacao_mandato",
        "path": os.path.join("docs", "Comunicacao_Mandato_Vereadores.pdf"),
        "persist": True,  # salva/recupera índice em ./indices/<name>
    },
    {
        "name": "perguntas_frequentes",
        "path": os.path.join("docs", "Perguntas Frequentes - Eu Vereador.pdf"),
        "persist": True,  # salva/recupera índice em ./indices/<name>
    },
    # Adicione novos aqui:
    # {"name": "planejamento_campanha", "path": "docs/Planejamento_Campanha.pdf", "persist": True},
]

# Pasta onde os índices FAISS ficam salvos (um subdir por tool)
INDICES_DIR = "indices"

# Parâmetros de chunking / retrieval
CHUNK_SIZE = 900
CHUNK_OVERLAP = 150
RETRIEVER_K = 4
