# Relatório de Teste - Reeleição em Cidade Pequena

## Informações do Teste

- **Data/Hora**: 12/01/2026 - 10:59
- **Configuração**: Reeleição + Cidade Pequena + Desafiador
- **Votos da Última Eleição**: 30.000
- **Screenshot**: `erro_reeleicao_pequena_desafiador.png`
- **CSV**: `erro_reeleicao_pequena_desafiador.csv`

## Configuração Esperada

### Parâmetros da Cidade Pequena
- **Faixa de eleitores**: Até 30.000
- **Média para cálculos**: 15.000 eleitores
- **Teto de gastos**: R$ 35.000

### Cálculos Esperados (Reeleição)
- **Votos Iniciais**: 30% dos votos da última eleição = 30% de 30.000 = **9.000 votos**
- **Meta de Votos**: 2% de 15.000 = **300 votos**
- **Contatos Iniciais**: Igual aos votos iniciais = **9.000 contatos**
- **Meta de Contatos**: 20% da meta de votos = 20% de 300 = **60 contatos**
- **Saldo Inicial**: 60% do teto = 60% de R$ 35.000 = **R$ 21.000**
- **Energia**: 100%
- **Reputação**: 50%

## Resultados Observados

| Parâmetro | Esperado | Observado | Status |
|-----------|----------|-----------|--------|
| Votos Iniciais | 9.000 | **0** | ❌ ERRO CRÍTICO |
| Meta de Votos | 300 | **400** | ❌ ERRO |
| Contatos Iniciais | 9.000 | **0** | ❌ ERRO CRÍTICO |
| Meta de Contatos | 60 | 80 | ❌ ERRO |
| Energia | 100% | 100% | ✅ OK |
| Reputação | 50% | 50% | ✅ OK |
| Saldo | R$ 21.000 | **R$ 10.000** | ❌ ERRO CRÍTICO |

## Erros Identificados

### 1. Votos Iniciais Zerados (CRÍTICO)
- **Esperado**: 9.000 votos (30% de 30.000)
- **Observado**: 0 votos
- **Diferença**: -9.000 votos (-100%)
- **Gravidade**: **CRÍTICA**
- **Impacto**: O sistema ignorou completamente o input de votos da última eleição
- **Consequência**: Reeleição funciona exatamente como primeira candidatura, eliminando a vantagem de ser incumbente

### 2. Contatos Iniciais Zerados (CRÍTICO)
- **Esperado**: 9.000 contatos (igual aos votos iniciais)
- **Observado**: 0 contatos
- **Diferença**: -9.000 contatos (-100%)
- **Gravidade**: **CRÍTICA**
- **Impacto**: Candidato à reeleição perde toda sua base de apoio
- **Consequência**: Não há diferença entre primeira candidatura e reeleição

### 3. Meta de Votos Incorreta
- **Esperado**: 300 votos
- **Observado**: 400 votos
- **Diferença**: +100 votos (+33,3%)
- **Impacto**: Meta mais difícil (mesmo erro do teste anterior)

### 4. Meta de Contatos Incorreta
- **Esperado**: 60 contatos
- **Observado**: 80 contatos
- **Diferença**: +20 contatos (+33,3%)
- **Impacto**: Meta mais difícil (mesmo erro do teste anterior)

### 5. Saldo Inicial Incorreto (CRÍTICO)
- **Esperado**: R$ 21.000 (60% de R$ 35.000)
- **Observado**: R$ 10.000
- **Diferença**: -R$ 11.000 (-52,4%)
- **Gravidade**: **ALTA**
- **Impacto**: Candidato à reeleição tem menos dinheiro que deveria
- **Nota**: Mesmo valor fixo de R$ 10.000 observado no teste anterior

## Análise

### Possíveis Causas

1. **Votos e Contatos Iniciais**: O sistema não está processando o campo de "votos da última eleição" ou não está aplicando o cálculo de 30%

2. **Saldo Inicial**: Confirmado que há um valor fixo de R$ 10.000 sendo aplicado, ignorando:
   - O tamanho da cidade
   - O tipo de candidatura (primeira vs reeleição)
   - A porcentagem correta (10% vs 60%)

3. **Metas**: Mesmo erro sistemático do teste anterior, sugerindo problema no cálculo base

### Impacto no Gameplay

- **Balanceamento Quebrado**: Reeleição deveria ser mais fácil (você já tem votos e contatos), mas está idêntica à primeira candidatura
- **Mecânica Inútil**: Não há incentivo para escolher reeleição se não há benefícios
- **Economia Incorreta**: Candidato à reeleição deveria ter 6x mais dinheiro (60% vs 10%), mas tem menos da metade

### Comparação com Primeira Candidatura

| Aspecto | Primeira Candidatura | Reeleição Esperada | Reeleição Observada |
|---------|---------------------|-------------------|---------------------|
| Votos Iniciais | 0 | 9.000 | **0** ❌ |
| Contatos Iniciais | 0 | 9.000 | **0** ❌ |
| Saldo | R$ 3.500 | R$ 21.000 | **R$ 10.000** ❌ |

**Conclusão**: A reeleição está funcionando como primeira candidatura, mas com saldo intermediário incorreto.

## Recomendações

### Prioridade ALTA
1. **Implementar processamento do campo de votos da última eleição**
   - Capturar o valor digitado pelo usuário
   - Calcular 30% desse valor
   - Aplicar aos votos e contatos iniciais

2. **Corrigir cálculo do saldo inicial**
   - Para reeleição: 60% do teto da cidade
   - Para primeira candidatura: 10% do teto da cidade
   - Eliminar o valor fixo de R$ 10.000

### Prioridade MÉDIA
3. **Corrigir cálculo das metas**
   - Verificar base de eleitores (deve ser 15.000 para cidade pequena)
   - Confirmar porcentagem (2% para votos)

## Próximos Passos

- Investigar o código que processa o formulário de reeleição
- Verificar se o valor de "votos da última eleição" está sendo salvo no banco
- Testar reeleição em outros tamanhos de cidade
- Verificar logs do backend para entender onde o cálculo está falhando
