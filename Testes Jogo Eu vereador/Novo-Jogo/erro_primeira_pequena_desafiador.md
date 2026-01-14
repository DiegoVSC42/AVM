# Relatório de Teste - Primeira Candidatura em Cidade Pequena

## Informações do Teste

- **Data/Hora**: 12/01/2026 - 10:54
- **Configuração**: Primeira Candidatura + Cidade Pequena + Desafiador
- **Screenshot**: `erro_primeira_pequena_desafiador.png`
- **CSV**: `erro_primeira_pequena_desafiador.csv`

## Configuração Esperada

### Parâmetros da Cidade Pequena
- **Faixa de eleitores**: Até 30.000
- **Média para cálculos**: 15.000 eleitores
- **Teto de gastos**: R$ 35.000

### Cálculos Esperados (Primeira Candidatura)
- **Votos Iniciais**: 0 (primeira candidatura sempre começa do zero)
- **Meta de Votos**: 2% de 15.000 = **300 votos**
- **Contatos Iniciais**: 0 (primeira candidatura)
- **Meta de Contatos**: 20% da meta de votos = 20% de 300 = **60 contatos**
- **Saldo Inicial**: 10% do teto = 10% de R$ 35.000 = **R$ 3.500**
- **Energia**: 100%
- **Reputação**: 50%

## Resultados Observados

| Parâmetro | Esperado | Observado | Status |
|-----------|----------|-----------|--------|
| Votos Iniciais | 0 | 0 | ✅ OK |
| Meta de Votos | 300 | **400** | ❌ ERRO |
| Contatos Iniciais | 0 | 0 | ✅ OK |
| Meta de Contatos | 60 | **80** | ❌ ERRO |
| Energia | 100% | 100% | ✅ OK |
| Reputação | 50% | 50% | ✅ OK |
| Saldo | R$ 3.500 | **R$ 10.000** | ❌ ERRO |

## Erros Identificados

### 1. Meta de Votos Incorreta
- **Esperado**: 300 votos (2% de 15.000)
- **Observado**: 400 votos
- **Diferença**: +100 votos (+33,3%)
- **Impacto**: Meta mais difícil que o esperado

### 2. Meta de Contatos Incorreta
- **Esperado**: 60 contatos (20% de 300)
- **Observado**: 80 contatos
- **Diferença**: +20 contatos (+33,3%)
- **Impacto**: Meta mais difícil que o esperado
- **Nota**: A proporção de 20% está sendo mantida em relação à meta de votos incorreta (20% de 400 = 80)

### 3. Saldo Inicial Incorreto (CRÍTICO)
- **Esperado**: R$ 3.500 (10% de R$ 35.000)
- **Observado**: R$ 10.000
- **Diferença**: +R$ 6.500 (+185,7%)
- **Impacto**: Jogador começa com quase 3x mais dinheiro que deveria
- **Gravidade**: **ALTA** - Afeta significativamente o balanceamento do jogo

## Análise

### Possíveis Causas

1. **Meta de Votos**: O sistema pode estar usando uma base de eleitores diferente (20.000 ao invés de 15.000) ou uma porcentagem diferente (2,67% ao invés de 2%)

2. **Saldo Inicial**: Parece haver um valor fixo de R$ 10.000 sendo aplicado independentemente do tamanho da cidade ou tipo de candidatura

### Impacto no Gameplay

- **Dificuldade**: As metas mais altas tornam o jogo mais difícil
- **Economia**: O saldo inicial muito maior facilita demais a campanha, quebrando o balanceamento
- **Progressão**: O jogador tem recursos excessivos para a primeira fase

## Recomendações

1. **Verificar cálculo da meta de votos**: Confirmar se está usando 2% da média correta (15.000 para cidade pequena)
2. **Corrigir saldo inicial**: Implementar cálculo dinâmico baseado no teto da cidade (10% de R$ 35.000)
3. **Revisar meta de contatos**: Ajustar para 20% da meta de votos corrigida

## Próximos Passos

- Testar outras combinações de cidade/dificuldade
- Verificar se o erro de saldo é sistemático em todas as configurações
- Analisar o código responsável pelos cálculos iniciais
