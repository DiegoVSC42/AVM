# pip install ollama
from ollama import Client

client = Client(host="http://localhost:11434")

stream = client.chat(
    model="mistral",  # ou 'mistral:latest'
    messages=[{"role": "user", "content": "Conte-me uma história"}],
    stream=True,
)

for chunk in stream:
    # cada chunk traz só o delta
    print(chunk["message"]["content"], end="", flush=True)
