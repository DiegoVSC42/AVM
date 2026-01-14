# 🤖 Script de Testes Automatizados - Eu Vereador Jogo

## 📋 Descrição

Este script automatiza completamente os testes do painel de criação de novo jogo, testando **todas as combinações possíveis** de:
- **Tipos de Candidatura**: Primeira Candidatura, Reeleição
- **Tamanhos de Cidade**: Pequena, Média, Grande, Metrópole
- **Níveis de Dificuldade**: Iniciante, Desafiador, Veterano

**Total de testes**: 2 × 4 × 3 = **24 combinações**

## 🔧 Pré-requisitos

1. **Python 3.7+** instalado
2. **Chrome** instalado
3. **Bibliotecas Python**:
   ```bash
   pip install selenium openpyxl
   ```
4. **ChromeDriver** (o Selenium geralmente baixa automaticamente)

## 🚀 Como Usar

### 1. Certifique-se de que o servidor local está rodando
```bash
# O jogo deve estar acessível em:
http://localhost:3000/novo-jogo
```

### 2. Execute o script
```bash
python teste_automatizado.py
```

### 3. Aguarde a execução
O script irá:
- ✅ Abrir o Chrome automaticamente
- ✅ Navegar para cada combinação de teste
- ✅ Preencher os formulários
- ✅ Iniciar o jogo
- ✅ Extrair os valores iniciais
- ✅ Comparar com os valores esperados
- ✅ Salvar tudo em uma planilha Excel

### 4. Verifique os resultados
A planilha será salva em:
```
Novo-Jogo/testes_automatizados_[timestamp].xlsx
```

## 📊 Formato da Planilha

A planilha gerada contém:
- **Configuração do teste**: Tipo, Cidade, Dificuldade
- **Valores Esperados vs Obtidos** para cada parâmetro:
  - Votos Iniciais e Meta
  - Contatos Iniciais e Meta
  - Energia
  - Reputação
  - Saldo
- **Status** de cada parâmetro (✅ OK ou ❌ ERRO)
- **Resultado Geral** (✅ PASSOU ou ❌ FALHOU)

## 🎨 Cores na Planilha

- 🟢 **Verde**: Valores corretos (✅ OK / ✅ PASSOU)
- 🔴 **Vermelho claro**: Valores incorretos (❌ ERRO)
- 🔴 **Vermelho escuro**: Teste falhou completamente (❌ FALHOU)

## ⚙️ Configurações

Você pode editar o arquivo `teste_automatizado.py` para:

### Alterar a URL do teste
```python
URL_BASE = "http://localhost:3000/novo-jogo"  # Altere aqui
```

### Alterar votos de reeleição
```python
{"nome": "Reeleição", "votos_ultima_eleicao": 30000}  # Altere o valor
```

### Testar apenas algumas combinações
Comente as linhas que não quer testar em `CONFIGURACOES`:
```python
"tamanhos_cidade": [
    {"nome": "Cidade Pequena", ...},
    # {"nome": "Cidade Média", ...},  # Comentado = não testa
    {"nome": "Cidade Grande", ...},
]
```

## 🐛 Solução de Problemas

### Erro: "ChromeDriver not found"
```bash
# Instale o webdriver-manager
pip install webdriver-manager

# Ou baixe manualmente em:
# https://chromedriver.chromium.org/
```

### Erro: "Element not found"
- Verifique se o jogo está rodando em `localhost:3000`
- Aumente os tempos de espera (`time.sleep()`) no script
- Verifique se a estrutura HTML do site não mudou

### Testes muito lentos
- Reduza os `time.sleep()` no script
- Use modo headless (navegador invisível):
  ```python
  chrome_options.add_argument("--headless")
  ```

## 📝 Exemplo de Saída

```
🚀 Iniciando testes automatizados...
🌐 URL: http://localhost:3000/novo-jogo
📋 Ambiente: LOCAL_AUTOMATIZADO

🔄 Testando: Primeira Candidatura + Cidade Pequena + Iniciante
✅ Teste concluído: {'votos_iniciais': 0, 'meta_votos': 300, ...}

🔄 Testando: Primeira Candidatura + Cidade Pequena + Desafiador
✅ Teste concluído: {'votos_iniciais': 0, 'meta_votos': 300, ...}

...

📊 Planilha salva em: Novo-Jogo/testes_automatizados_1768239876.xlsx

✅ Testes concluídos!
📊 Total: 24 | Passou: 24 | Falhou: 0

🔒 Navegador fechado
```

## 🎯 Próximos Passos

Depois de rodar o script, você pode:
1. Abrir a planilha Excel gerada
2. Filtrar por testes que falharam (❌ FALHOU)
3. Investigar os erros específicos
4. Gerar relatórios individuais para cada erro (se necessário)

## 💡 Dicas

- Execute o script quando não estiver usando o computador (demora ~10-15 minutos)
- Não mexa no mouse/teclado durante a execução
- Feche outras abas do Chrome para melhor performance
- Rode primeiro em LOCAL, depois em PRODUÇÃO (alterando a URL)
