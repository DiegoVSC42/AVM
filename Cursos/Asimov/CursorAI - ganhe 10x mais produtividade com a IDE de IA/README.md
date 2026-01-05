# 🧮 Calculadora Python

Uma calculadora interativa em Python que realiza operações matemáticas básicas e avançadas através de uma interface de linha de comando.

## 📋 Descrição

Esta calculadora permite realizar diversos tipos de cálculos matemáticos de forma simples e intuitiva. Você pode digitar expressões matemáticas diretamente e obter resultados instantâneos.

## ✨ Funcionalidades

### Operações Básicas
- **Adição** (`+`): Soma dois números
- **Subtração** (`-`): Subtrai dois números
- **Multiplicação** (`*`): Multiplica dois números
- **Divisão** (`/`): Divide dois números (divisão decimal)
- **Divisão Inteira** (`//`): Retorna apenas a parte inteira da divisão
- **Módulo** (`%`): Retorna o resto da divisão
- **Potenciação** (`**`): Eleva um número à potência de outro

### Operações Avançadas
- **Raiz Quadrada** (`sqrt()`): Calcula a raiz quadrada de um número
- **Seno** (`sin()`): Calcula o seno de um ângulo em graus
- **Cosseno** (`cos()`): Calcula o cosseno de um ângulo em graus
- **Tangente** (`tan()`): Calcula a tangente de um ângulo em graus
- **Logaritmo** (`log()`): Calcula logaritmo natural ou com base customizada

## 🔧 Requisitos

- Python 3.6 ou superior
- Módulos padrão do Python:
  - `math` (já incluído no Python)
  - `re` (já incluído no Python)

## 📦 Instalação

1. Clone o repositório ou baixe o arquivo `calculadora.py`:
```bash
git clone https://github.com/DiegoVSC42/calculadora.git
cd calculadora
```

2. Certifique-se de ter o Python instalado:
```bash
python --version
```

## 🚀 Como Usar

### Executar a Calculadora

Execute o arquivo Python diretamente:

```bash
python calculadora.py
```

### Formato de Entrada

A calculadora aceita expressões matemáticas em dois formatos:

#### 1. Operações Binárias (dois números)
Digite a expressão diretamente no formato: `número1 operador número2`

**Exemplos:**
```
2+2
10/5
5*3
8-3
2**3
10//3
10%3
```

#### 2. Operações Unárias (funções)
Digite a função seguida do número entre parênteses: `função(número)`

**Exemplos:**
```
sqrt(16)
sin(30)
cos(45)
tan(60)
log(10)
log(100, 10)  # Logaritmo com base customizada
```

### Encerrar a Calculadora

Digite `sair` quando quiser encerrar o programa.

## 📝 Exemplos de Uso

### Operações Básicas

```
Entrada: 2+2
Saída: 2.0 + 2.0 = 4.0

Entrada: 10/5
Saída: 10.0 / 5.0 = 2.0

Entrada: 5*3
Saída: 5.0 * 3.0 = 15.0

Entrada: 2**3
Saída: 2.0 ** 3.0 = 8.0

Entrada: 10//3
Saída: 10.0 // 3.0 = 3.0

Entrada: 10%3
Saída: 10.0 % 3.0 = 1.0
```

### Operações Avançadas

```
Entrada: sqrt(16)
Saída: sqrt(16.0) = 4.0

Entrada: sin(30)
Saída: sin(30.0) = 0.5

Entrada: cos(45)
Saída: cos(45.0) = 0.7071067811865476

Entrada: tan(60)
Saída: tan(60.0) = 1.7320508075688767

Entrada: log(10)
Saída: ln(10.0) = 2.302585092994046

Entrada: log(100, 10)
Saída: log(100.0, 10.0) = 2.0
```

## ⚠️ Tratamento de Erros

A calculadora possui tratamento de erros para casos especiais:

- **Divisão por zero**: Retorna mensagem de erro ao tentar dividir por zero
- **Raiz quadrada de número negativo**: Retorna mensagem de erro
- **Logaritmo de número não positivo**: Retorna mensagem de erro
- **Expressão inválida**: Retorna mensagem de erro com exemplos válidos

## 📂 Estrutura do Código

O projeto consiste em um único arquivo `calculadora.py` com as seguintes funções:

- **`calcular(num1, num2, operacao)`**: Executa o cálculo matemático baseado na operação fornecida
- **`parsear_expressao(expressao)`**: Faz o parsing da expressão matemática inserida pelo usuário
- **`exibir_menu()`**: Exibe o menu com instruções e exemplos
- **`main()`**: Função principal que controla o loop da calculadora

## 🎯 Características Técnicas

- Interface interativa em loop contínuo
- Validação de entrada do usuário
- Suporte a números decimais (float)
- Funções trigonométricas em graus (conversão automática para radianos)
- Logaritmo natural (base e) ou com base customizada
- Tratamento robusto de exceções

## 📌 Observações Importantes

1. **Funções Trigonométricas**: Os valores são inseridos em **graus**, mas a calculadora converte automaticamente para radianos internamente.

2. **Logaritmo**: 
   - `log(10)` calcula o logaritmo natural (base e)
   - `log(100, 10)` calcula o logaritmo de 100 na base 10

3. **Espaços**: Espaços na expressão são ignorados automaticamente.

4. **Case Insensitive**: As funções podem ser digitadas em maiúsculas ou minúsculas (ex: `SQRT(16)` ou `sqrt(16)`).

## 🤝 Contribuindo

Sinta-se à vontade para fazer fork, criar issues ou enviar pull requests!

## 📄 Licença

Este projeto é de código aberto e está disponível para uso livre.

---

**Desenvolvido com Python** 🐍
