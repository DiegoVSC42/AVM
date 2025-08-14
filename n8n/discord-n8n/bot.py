import discord
import requests
from datetime import datetime

TOKEN = "MTQwNTIyNjIxNjQ5OTMxNDgyMA.G8Kst2.20dOEgxDOFY-6wJ1fhkYEMXB3ktjDmnVhgnbyg"  # Troque pelo token válido e seguro
WEBHOOK_URL = "http://localhost:5678/webhook/discord-event"

intents = discord.Intents.default()
intents.voice_states = True

client = discord.Client(intents=intents)


def log(msg):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"[{agora}] {msg}")


def enviar_webhook(user, canal):
    payload = {
        "user": user,
        "canal": canal,
        "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    }
    log(f"Tentando enviar: {payload}")
    try:
        r = requests.post(WEBHOOK_URL, json=payload, timeout=5)
        if r.status_code == 200:
            log("✅ Envio para webhook concluído com sucesso")
        else:
            log(f"⚠️ Erro no envio: status {r.status_code} - {r.text}")
    except Exception as e:
        log(f"❌ Falha ao enviar para webhook: {e}")


@client.event
async def on_ready():
    log(f"{client.user} conectado!")


@client.event
async def on_voice_state_update(member, before, after):
    # Entrou em um canal (estava fora)
    if before.channel is None and after.channel is not None:
        log(f"{member.name} entrou em {after.channel.name}")
        enviar_webhook(member.name, after.channel.name)

    # Mudou de canal
    elif (
        before.channel is not None
        and after.channel is not None
        and before.channel != after.channel
    ):
        log(f"{member.name} mudou de {before.channel.name} para {after.channel.name}")
        enviar_webhook(member.name, after.channel.name)

    # Saiu do canal
    elif before.channel is not None and after.channel is None:
        log(f"{member.name} saiu de {before.channel.name}")
        enviar_webhook(member.name, "Saiu do canal")


client.run(TOKEN)
