
import os
from dotenv import load_dotenv

load_dotenv(override=True)

# Modelos no Ollama
OLLAMA_LLM_MODEL = os.getenv("OLLAMA_LLM_MODEL", "mistral")
OLLAMA_EMBED_MODEL = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")

# Caminhos
DOCS_DIR = os.getenv("DOCS_DIR", "./documentos_curso")
CHROMA_DIR = os.getenv("CHROMA_DIR", "./chroma_db")

# Chunking
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1000"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "150"))

# Recuperação
TOP_K_VECTOR = int(os.getenv("TOP_K_VECTOR", "5"))
TOP_K_BM25 = int(os.getenv("TOP_K_BM25", "5"))
ALPHA_ENSEMBLE = float(os.getenv("ALPHA_ENSEMBLE", "0.6"))

# Memória
MEMORY_WINDOW = int(os.getenv("MEMORY_WINDOW", "6"))
