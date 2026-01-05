#!/usr/bin/env python3
"""Script para diagnosticar problemas com .env e OpenAI API"""

import os
from pathlib import Path

print("=== DIAGNÓSTICO DO .env ===\n")

# 1. Verificar se o arquivo .env existe
env_path = Path('.env')
print(f"1. Arquivo .env existe? {env_path.exists()}")
if env_path.exists():
    print(f"   Localização: {env_path.absolute()}")
    # Mostrar conteúdo (sem revelar a chave completa)
    with open(env_path) as f:
        content = f.read()
        if 'OPENAI_API_KEY' in content:
            print("   ✓ OPENAI_API_KEY encontrada no arquivo")
        else:
            print("   ✗ OPENAI_API_KEY NÃO encontrada no arquivo")
else:
    print("   ✗ Arquivo .env não encontrado!")

print("\n2. Testando carregamento com python-dotenv:")
try:
    from dotenv import load_dotenv
    resultado = load_dotenv()
    print(f"   load_dotenv() retornou: {resultado}")
    
    # Verificar se a variável foi carregada
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        # Mostrar apenas os primeiros e últimos caracteres
        masked = f"{api_key[:7]}...{api_key[-4:]}" if len(api_key) > 11 else "***"
        print(f"   ✓ OPENAI_API_KEY carregada: {masked}")
        print(f"   Comprimento da chave: {len(api_key)} caracteres")
        
        # Verificar se começa com sk-
        if api_key.startswith('sk-'):
            print("   ✓ Chave começa com 'sk-' (formato correto)")
        else:
            print("   ✗ Chave NÃO começa com 'sk-' (pode estar incorreta)")
    else:
        print("   ✗ OPENAI_API_KEY não foi carregada")
        
except ImportError:
    print("   ✗ python-dotenv não está instalado")
    print("   Execute: pip install python-dotenv")

print("\n3. Verificando variáveis de ambiente do sistema:")
if "OPENAI_API_KEY" in os.environ:
    api_key = os.environ["OPENAI_API_KEY"]
    masked = f"{api_key[:7]}...{api_key[-4:]}" if len(api_key) > 11 else "***"
    print(f"   ✓ OPENAI_API_KEY está nas variáveis de ambiente: {masked}")
else:
    print("   ✗ OPENAI_API_KEY não está nas variáveis de ambiente do sistema")

print("\n4. Testando conexão com OpenAI:")
try:
    from langchain_openai import OpenAI
    
    # Tentar criar o cliente
    llm = OpenAI(temperature=0, max_tokens=10)
    print("   ✓ Cliente OpenAI criado com sucesso")
    
    # Tentar fazer uma chamada simples
    try:
        resposta = llm.invoke("Diga apenas 'OK'")
        print("   ✓ Conexão com API funcionando!")
        print(f"   Resposta: {resposta[:50]}")
    except Exception as e:
        print(f"   ✗ Erro ao chamar API: {str(e)[:100]}")
        
except ImportError:
    print("   ✗ langchain-openai não está instalado")
    print("   Execute: pip install langchain-openai")
except Exception as e:
    print(f"   ✗ Erro: {str(e)[:150]}")

print("\n=== FIM DO DIAGNÓSTICO ===")