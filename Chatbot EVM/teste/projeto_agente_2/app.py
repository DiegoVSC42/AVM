import chainlit as cl
from agent import AgenteMultiRAG

# Botões iniciais
ACOES_INICIAIS = [
    cl.Action(name="listar_tools", payload={}, label="📚 Ver documentos"),
    cl.Action(name="abrir_troca", payload={}, label="🔁 Trocar documento"),
]


@cl.on_chat_start
async def on_chat_start():
    agente = AgenteMultiRAG()
    agente.carregar_tools()
    cl.user_session.set("agente", agente)

    await cl.Message(
        "Oi, vereador! 👋 Posso te ajudar com o Eu Vereador Mandato."
    ).send()
    await cl.Message("Manda sua pergunta aqui no chat.", actions=ACOES_INICIAIS).send()

    # Mostra docs disponíveis (curto)
    await cl.Message(agente.listar_tools()).send()


@cl.on_message
async def on_message(message: cl.Message):
    agente: AgenteMultiRAG = cl.user_session.get("agente")
    if not agente:
        await cl.Message("Erro: agente não carregado.").send()
        return

    texto = (message.content or "").strip()
    if not texto:
        await cl.Message("Pode mandar sua pergunta.").send()
        return

    resposta = agente.responder(texto)
    await cl.Message(resposta).send()


# ======== Callbacks de ações (Chainlit 1.x) ========


@cl.action_callback("listar_tools")
async def ac_listar_tools(action: cl.Action):
    agente: AgenteMultiRAG = cl.user_session.get("agente")
    if not agente:
        await cl.Message("Erro: agente não carregado.").send()
        return
    await cl.Message(agente.listar_tools()).send()


@cl.action_callback("abrir_troca")
async def ac_abrir_troca(action: cl.Action):
    agente: AgenteMultiRAG = cl.user_session.get("agente")
    if not agente:
        await cl.Message("Erro: agente não carregado.").send()
        return

    nomes = list(agente.tools.keys())
    if not nomes:
        await cl.Message("Nenhum documento carregado.").send()
        return

    # Envia uma mensagem com botões de cada tool
    botoes = [
        cl.Action(name="use_tool", payload={"tool": n}, label=f"✅ {n}") for n in nomes
    ]
    await cl.Message("Qual documento você quer usar?", actions=botoes).send()


@cl.action_callback("use_tool")
async def ac_use_tool(action: cl.Action):
    agente: AgenteMultiRAG = cl.user_session.get("agente")
    if not agente:
        await cl.Message("Erro: agente não carregado.").send()
        return

    nome = (action.payload or {}).get("tool")
    if not nome:
        await cl.Message("Não entendi qual documento usar.").send()
        return

    msg = agente.set_active(nome)
    await cl.Message(msg).send()
