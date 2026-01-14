import asyncio
from pathlib import Path

from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
load_dotenv()

from fastmcp import Client

caminho_servidor = "http://localhost:8000/sse"

cliente = Client(caminho_servidor)

async def testar_servidor(cliente, busca):
    
    # Configurar o cliente da nova biblioteca
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    
    async with cliente:
        argumentos = {"busca": busca}
        resultado = await cliente.call_tool("buscar_wikipedia", arguments=argumentos)
        print(f"\n{resultado}\n")
        
        mensagem_sistema = f"""
        Você é um assistente de busca de informações na Wikipedia.
        
        o usuário buscou por: {busca}
        
        para esta busca, você encontrou a seguinte informação:
        {resultado.data}
        
        responda de forma amigável ao usuário.
        """
        
        response = await client.aio.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents="Pode me falar mais sobre o assunto?",
            config=types.GenerateContentConfig(
                system_instruction=mensagem_sistema
            )
        )
        
        print(response.text)

if __name__ == "__main__":
    asyncio.run(testar_servidor(cliente=cliente, busca="Isaac Newton"))