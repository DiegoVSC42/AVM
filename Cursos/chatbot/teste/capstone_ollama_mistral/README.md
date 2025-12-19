
# Capstone — Assistente RAG (sem RAGAS) com Ollama (Mistral)

Este projeto cria um assistente de perguntas e respostas usando **RAG** (Geração Aumentada por Recuperação)
com **Ollama** rodando localmente e o modelo **mistral** para geração. Avaliação automática (RAGAS) foi removida.

## Visão geral

- **Ingestão**: carrega PDFs da pasta `documentos_curso/`, divide em *chunks* e indexa no **Chroma**.
- **Busca híbrida**: combina semântica (vetorial) e lexical (BM25) via `EnsembleRetriever`.
- **Geração**: usa `ChatOllama` com `mistral`.
- **Memória**: histórico curto da conversa.
- **Arquivos separados por responsabilidade.**

## Estrutura
```
capstone_ollama_mistral/
├─ main.py                  # Ponto de entrada (onde você faz as perguntas)
├─ config.py                # Configurações (modelos, caminhos, parâmetros)
├─ ingestion.py             # Carregamento de PDFs e criação do índice no Chroma
├─ retrieval.py             # Recuperadores (vetorial, BM25 e ensemble)
├─ chain.py                 # Montagem da cadeia de conversação com recuperação
├─ utils.py                 # Funções utilitárias (limpeza, logs simples, etc.)
├─ requirements.txt
├─ README.md
├─ .env.example             # Exemplo de variáveis de ambiente
└─ documentos_curso/        # Coloque aqui seus PDFs
```
> Obs.: A pasta `documentos_curso/` pode ser criada automaticamente na primeira execução, caso não exista.

## Pré‑requisitos

1. **Python 3.10+**
2. **Ollama** instalado e rodando (https://ollama.com)
3. Baixe o modelo de geração **mistral** e um modelo de *embedding*. Por exemplo:
   ```bash
   ollama pull mistral
   ollama pull nomic-embed-text
   ```

## Instalação
```bash
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Primeiro uso (indexação)
Coloque seus **PDFs** dentro de `documentos_curso/` e rode:
```bash
python ingestion.py
```
Isso cria/atualiza o índice vetorial no `./chroma_db/`.

## Rodando o chat
```bash
python main.py
```
Depois digite suas perguntas. Para sair, use `sair`.

## Variáveis de ambiente
Copie `.env.example` para `.env` se quiser alterar padrões. Caso não exista `.env`, o projeto usa os defaults do `config.py`.
