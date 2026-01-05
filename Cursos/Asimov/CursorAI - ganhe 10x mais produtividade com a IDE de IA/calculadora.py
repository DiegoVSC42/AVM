import math
import re
from fractions import Fraction

def calcular(num1, num2, operacao):
    """
    Realiza cálculos matemáticos básicos e avançados.
    
    Args:
        num1: Primeiro número
        num2: Segundo número (ou None para operações unárias)
        operacao: Operação a ser realizada
    
    Returns:
        Resultado do cálculo
    """
    try:
        if operacao == '+':
            return num1 + num2
        elif operacao == '-':
            return num1 - num2
        elif operacao == '*':
            return num1 * num2
        elif operacao == '/':
            if num2 == 0:
                return "Erro: Divisão por zero!"
            return num1 / num2
        elif operacao == '//':
            if num2 == 0:
                return "Erro: Divisão por zero!"
            return num1 // num2
        elif operacao == '%':
            if num2 == 0:
                return "Erro: Divisão por zero!"
            return num1 % num2
        elif operacao == '**':
            return num1 ** num2
        elif operacao == 'sqrt':
            if num1 < 0:
                return "Erro: Não é possível calcular raiz quadrada de número negativo!"
            return math.sqrt(num1)
        elif operacao == 'log':
            if num1 <= 0:
                return "Erro: Logaritmo só pode ser calculado para números positivos!"
            if num2 and num2 > 0:
                return math.log(num1, num2)
            return math.log(num1)
        elif operacao == 'sin':
            return math.sin(math.radians(num1))
        elif operacao == 'cos':
            return math.cos(math.radians(num1))
        elif operacao == 'tan':
            return math.tan(math.radians(num1))
        else:
            return "Erro: Operação inválida!"
    except Exception as e:
        return f"Erro: {str(e)}"

def resultado_trig_para_fracao(resultado, operacao, angulo_graus, tolerancia=1e-9):
    """
    Converte resultado trigonométrico para fração exata quando possível.
    
    Args:
        resultado: Valor numérico do resultado trigonométrico
        operacao: 'sin', 'cos' ou 'tan'
        angulo_graus: Ângulo em graus
        tolerancia: Tolerância para comparação
    
    Returns:
        String com representação fracionária ou None
    """
    # Verifica se o resultado é numérico
    if isinstance(resultado, str) or not isinstance(resultado, (int, float)):
        return None
    
    # Normaliza o ângulo para 0-360°
    angulo_normalizado = angulo_graus % 360
    if angulo_normalizado < 0:
        angulo_normalizado += 360
    
    # Tabela de valores exatos para arcos notáveis (valores absolutos)
    valores_base = {
        # sin - valores absolutos
        (30, 'sin'): '1/2',
        (150, 'sin'): '1/2',
        (210, 'sin'): '1/2',  # negativo
        (330, 'sin'): '1/2',  # negativo
        (45, 'sin'): '√2/2',
        (135, 'sin'): '√2/2',
        (225, 'sin'): '√2/2',  # negativo
        (315, 'sin'): '√2/2',  # negativo
        (60, 'sin'): '√3/2',
        (120, 'sin'): '√3/2',
        (240, 'sin'): '√3/2',  # negativo
        (300, 'sin'): '√3/2',  # negativo
        (0, 'sin'): '0',
        (180, 'sin'): '0',
        (360, 'sin'): '0',
        (90, 'sin'): '1',
        (270, 'sin'): '1',  # negativo
        
        # cos - valores absolutos
        (60, 'cos'): '1/2',
        (300, 'cos'): '1/2',
        (120, 'cos'): '1/2',  # negativo
        (240, 'cos'): '1/2',  # negativo
        (45, 'cos'): '√2/2',
        (315, 'cos'): '√2/2',
        (135, 'cos'): '√2/2',  # negativo
        (225, 'cos'): '√2/2',  # negativo
        (30, 'cos'): '√3/2',
        (330, 'cos'): '√3/2',
        (150, 'cos'): '√3/2',  # negativo
        (210, 'cos'): '√3/2',  # negativo
        (90, 'cos'): '0',
        (270, 'cos'): '0',
        (0, 'cos'): '1',
        (360, 'cos'): '1',
        (180, 'cos'): '1',  # negativo
        
        # tan - valores absolutos
        (30, 'tan'): '√3/3',
        (210, 'tan'): '√3/3',
        (45, 'tan'): '1',
        (225, 'tan'): '1',
        (60, 'tan'): '√3',
        (240, 'tan'): '√3',
        (0, 'tan'): '0',
        (180, 'tan'): '0',
        (360, 'tan'): '0',
    }
    
    # Verifica se o ângulo corresponde a um valor exato
    chave = (int(round(angulo_normalizado)), operacao)
    if chave in valores_base:
        valor_base_str = valores_base[chave]
        
        # Calcula o valor esperado (absoluto)
        if valor_base_str == '1/2':
            valor_base = 0.5
        elif valor_base_str == '√2/2':
            valor_base = math.sqrt(2) / 2
        elif valor_base_str == '√3/2':
            valor_base = math.sqrt(3) / 2
        elif valor_base_str == '√3/3':
            valor_base = math.sqrt(3) / 3
        elif valor_base_str == '√3':
            valor_base = math.sqrt(3)
        elif valor_base_str == '1':
            valor_base = 1.0
        elif valor_base_str == '0':
            valor_base = 0.0
        else:
            return None
        
        # Verifica se o resultado corresponde ao valor esperado (considerando sinal)
        # Usa uma tolerância maior para comparação de ponto flutuante
        diferenca = abs(abs(resultado) - valor_base)
        if diferenca < tolerancia or diferenca < 1e-9:
            # Determina o sinal correto
            if abs(resultado) < tolerancia:
                return '0'
            elif resultado < -tolerancia:
                return f"-{valor_base_str}"
            else:
                return valor_base_str
    
    return None

def radianos_para_fracao_pi(radianos, tolerancia=1e-6):
    """
    Converte radianos para fração de π quando possível.
    
    Args:
        radianos: Valor em radianos
        tolerancia: Tolerância para comparação de valores
    
    Returns:
        String com a representação fracionária de π ou None se não for possível
    """
    if abs(radianos) < tolerancia:
        return "0"
    
    # Divide por π para obter o coeficiente
    coeficiente = radianos / math.pi
    
    # Tenta encontrar uma fração simples
    # Lista de frações comuns de π (arcos notáveis)
    fracoes_comuns = [
        (0, "0"),
        (1/6, "π/6"),      # 30°
        (1/4, "π/4"),      # 45°
        (1/3, "π/3"),      # 60°
        (1/2, "π/2"),      # 90°
        (2/3, "2π/3"),     # 120°
        (3/4, "3π/4"),     # 135°
        (5/6, "5π/6"),     # 150°
        (1, "π"),          # 180°
        (3/2, "3π/2"),     # 270°
        (2, "2π"),         # 360°
        (-1/6, "-π/6"),
        (-1/4, "-π/4"),
        (-1/3, "-π/3"),
        (-1/2, "-π/2"),
        (-2/3, "-2π/3"),
        (-3/4, "-3π/4"),
        (-5/6, "-5π/6"),
        (-1, "-π"),
        (-3/2, "-3π/2"),
        (-2, "-2π"),
    ]
    
    # Verifica se o coeficiente corresponde a uma fração comum
    for frac_valor, frac_str in fracoes_comuns:
        if abs(coeficiente - frac_valor) < tolerancia:
            return frac_str
    
    # Tenta simplificar como fração
    try:
        # Converte para Fraction e simplifica
        frac = Fraction(coeficiente).limit_denominator(12)
        
        # Se o denominador for razoável e a fração for exata
        if frac.denominator <= 12 and abs(float(frac) - coeficiente) < tolerancia:
            num = abs(frac.numerator)
            den = frac.denominator
            
            if frac.numerator == 0:
                return "0"
            elif frac.numerator < 0:
                sinal = "-"
            else:
                sinal = ""
            
            if num == 1 and den == 1:
                return f"{sinal}π"
            elif num == 1:
                return f"{sinal}π/{den}"
            elif den == 1:
                return f"{sinal}{num}π"
            else:
                return f"{sinal}{num}π/{den}"
    except:
        pass
    
    return None

def parsear_expressao(expressao):
    """
    Faz o parsing de uma expressão matemática e retorna os componentes.
    
    Suporta:
    - Operações binárias: 2+2, 10/5, 5*3, 8-3, 2**3, 10//3, 10%3
    - Operações unárias: sqrt(16), sin(30), cos(45), tan(60), log(10)
    - Logaritmo com base: log(100, 10)
    
    Returns:
        Tupla (num1, num2, operacao) ou None se não conseguir fazer parsing
    """
    expressao = expressao.strip().replace(' ', '')
    
    # Operações unárias com parênteses: sqrt(16), sin(30), etc.
    padrao_unario = r'^(sqrt|sin|cos|tan|log)\(([-+]?\d*\.?\d+)(?:,\s*([-+]?\d*\.?\d+))?\)$'
    match = re.match(padrao_unario, expressao, re.IGNORECASE)
    if match:
        operacao = match.group(1).lower()
        num1 = float(match.group(2))
        num2 = float(match.group(3)) if match.group(3) else None
        return (num1, num2, operacao)
    
    # Operações binárias: 2+2, 10/5, 5*3, 8-3, 2**3, 10//3, 10%3
    # Ordem importante: ** antes de *, // antes de /
    operadores = [
        ('**', '**'),
        ('//', '//'),
        ('*', '*'),
        ('/', '/'),
        ('%', '%'),
        ('+', '+'),
        ('-', '-')
    ]
    
    for op_simbolo, op_nome in operadores:
        if op_simbolo in expressao:
            partes = expressao.split(op_simbolo, 1)
            if len(partes) == 2:
                try:
                    num1 = float(partes[0])
                    num2 = float(partes[1])
                    return (num1, num2, op_nome)
                except ValueError:
                    continue
    
    return None

def exibir_menu():
    """Exibe o menu de operações disponíveis."""
    print("\n" + "="*50)
    print("          CALCULADORA SIMPLES")
    print("="*50)
    print("\nDigite uma expressao matematica diretamente!")
    print("\nExemplos:")
    print("  2+2          -> 4")
    print("  10/5         -> 2")
    print("  5*3          -> 15")
    print("  2**3         -> 8 (potencia)")
    print("  sqrt(16)     -> 4")
    print("  sin(30)      -> 0.5")
    print("  log(100, 10) -> 2")
    print("\nOperações disponíveis:")
    print("  +, -, *, /, //, %, **")
    print("  sqrt(), sin(), cos(), tan(), log()")
    print("  sair: Para encerrar a calculadora")
    print("="*50)

def main():
    """Função principal da calculadora."""
    print("Bem-vindo à Calculadora Python!")
    
    while True:
        exibir_menu()
        
        entrada = input("\nDigite uma expressão (ex: 2+2, 10/5, sqrt(16)): ").strip()
        
        if entrada.lower() == 'sair':
            print("\nObrigado por usar a calculadora! Até logo!")
            break
        
        if not entrada:
            print("Erro: Por favor, digite uma expressão válida!")
            input("\nPressione Enter para continuar...")
            continue
        
        # Tenta fazer parsing da expressão
        resultado_parse = parsear_expressao(entrada)
        
        if resultado_parse:
            num1, num2, operacao = resultado_parse
            
            # Executa o cálculo
            resultado = calcular(num1, num2, operacao)
            
            # Exibe o resultado formatado
            if operacao in ['sin', 'cos', 'tan']:
                # Funções trigonométricas: mostra ângulo em fração de π e valor numérico
                angulo_rad = math.radians(num1)
                frac_pi = radianos_para_fracao_pi(angulo_rad)
                resultado_frac = resultado_trig_para_fracao(resultado, operacao, num1)
                
                print(f"\n{operacao}({num1}°) = ", end="")
                if resultado_frac:
                    print(f"{resultado_frac} ou {resultado}")
                else:
                    print(f"{resultado}")
                
                if frac_pi:
                    print(f"  Ângulo: {frac_pi} rad ou {angulo_rad}")
                else:
                    print(f"  Ângulo: {angulo_rad} rad")
            elif operacao == 'sqrt':
                print(f"\nsqrt({num1}) = {resultado}")
            elif operacao == 'log':
                if num2:
                    print(f"\nlog({num1}, {num2}) = {resultado}")
                else:
                    print(f"\nln({num1}) = {resultado}")
            elif operacao == '+':
                print(f"\n{num1} + {num2} = {resultado}")
            elif operacao == '-':
                print(f"\n{num1} - {num2} = {resultado}")
            elif operacao == '*':
                print(f"\n{num1} * {num2} = {resultado}")
            elif operacao == '/':
                print(f"\n{num1} / {num2} = {resultado}")
            elif operacao == '//':
                print(f"\n{num1} // {num2} = {resultado}")
            elif operacao == '%':
                print(f"\n{num1} % {num2} = {resultado}")
            elif operacao == '**':
                print(f"\n{num1} ** {num2} = {resultado}")
            else:
                print(f"\n{num1} {operacao} {num2} = {resultado}")
        else:
            print(f"Erro: Não foi possível interpretar a expressão '{entrada}'")
            print("Exemplos válidos: 2+2, 10/5, sqrt(16), sin(30)")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
