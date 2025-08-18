# tools/comunicacao.py
from langchain_core.tools import tool
from vetores import vector_store_comunicacao
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

# usa o vetor que você já monta em vetores.py
from vetores import vector_store_comunicacao


@tool("pega_contexto_comunicacao")
def rag_chain_clara():
    """
    Cadeia RAG fixa no documento de Comunicação de Mandato para Vereadores.
    Sempre usa o vetor e NUNCA consulta internet.
    Retorna uma chain que você invoca com: chain.invoke({"input": pergunta})
    """

    # 1) Modelo (pode trocar para "llama3" se preferir)
    model = ChatOllama(model="mistral", temperature=0.2)

    # 2) Prompt em PT-BR, curto e com regra de não inventar
    prompt = ChatPromptTemplate.from_template(
        """
        Você é a Clara, atendente virtual do curso Comunicação Estratégica de Mandato para Vereadores.
        Fale como no WhatsApp: direto, simples e acolhedor. Frases curtas (2–3 linhas).

        Regras:
        - Responda SOMENTE com base no contexto abaixo.
        - Se a resposta não estiver no contexto, diga exatamente:
          "Não encontrei essa informação no material do curso."
        - Não explique processo. Não cite ferramentas. Não invente.

        Pergunta: {input}

        Contexto:
        {context}

        Resposta:
        """
    )

    # 3) Retriever do seu vetor (sempre consulta o PDF)
    # use k 5–8 conforme densidade do material
    retriever = vector_store_comunicacao.as_retriever(
        search_type="similarity",  # estável pro InMemoryVectorStore
        search_kwargs={"k": 6},
    )

    # 4) Monta a chain de documentos e a chain final de recuperação
    document_chain = create_stuff_documents_chain(model, prompt)
    chain = create_retrieval_chain(retriever, document_chain)

    return chain


# def pega_contexto_comunicacao(query: str) -> str:
#     """Recupera trechos do material do curso que respondam à dúvida do usuário."""
#     retriever = vector_store_comunicacao.as_retriever(search_kwargs={"k": 4})
#     docs = retriever.get_relevant_documents(query)
#     if not docs:
#         return "Não encontrei essa informação no material do curso."
#     return "\n\n---\n\n".join(d.page_content for d in docs)
