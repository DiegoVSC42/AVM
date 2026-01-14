# 🧮 Calculadora Python - Interface Web com Streamlit

Interface web moderna para a Calculadora Python usando Streamlit.

## 🚀 Como Executar

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Executar a aplicação

```bash
streamlit run app.py
```

A aplicação será aberta automaticamente no navegador em `http://localhost:8501`

## ✨ Funcionalidades da Interface

- **Interface Moderna**: Design limpo e responsivo
- **Entrada de Expressões**: Campo de texto para digitar expressões matemáticas
- **Botões de Funções Rápidas**: Acesso rápido a funções trigonométricas e outras operações
- **Exibição de Resultados**: 
  - Resultados em frações exatas para trigonometria (1/2, √2/2, √3/2, etc.)
  - Ângulos em frações de π (π/6, π/4, π/3, etc.)
  - Valores numéricos
- **Histórico de Cálculos**: Mantém os últimos 20 cálculos realizados
- **Reutilização**: Clique em "Usar" para reutilizar uma expressão do histórico

## 📝 Exemplos de Uso

### Operações Básicas
- `2+2`
- `10/5`
- `5*3`
- `2**3`
- `10//3`
- `10%3`

### Operações Avançadas
- `sqrt(16)`
- `sin(30)`
- `cos(45)`
- `tan(60)`
- `log(10)`
- `log(100, 10)`

## 🎨 Características Visuais

- Design com gradiente moderno
- Cores diferenciadas para frações exatas e ângulos
- Layout responsivo
- Sidebar com informações e exemplos
- Histórico expansível

## 📋 Requisitos

- Python 3.6 ou superior
- Streamlit 1.28.0 ou superior
- Módulos padrão do Python (math, re, fractions)

## 🔧 Estrutura

- `app.py`: Interface Streamlit principal
- `calculadora.py`: Lógica da calculadora (importada)
- `requirements.txt`: Dependências do projeto

## 💡 Dicas

1. Use os botões de funções rápidas para inserir funções com mais facilidade
2. O histórico mantém os últimos 20 cálculos
3. Clique em "Usar" em um item do histórico para reutilizar a expressão
4. Para trigonometria, os resultados são exibidos em frações exatas quando aplicável
