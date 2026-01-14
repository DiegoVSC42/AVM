# Relatório de Teste - Primeira Candidatura em Cidade Média

## Informações do Teste

- **Data/Hora**: 12/01/2026 - 11:03
- **Configuração**: Primeira Candidatura + Cidade Média + Desafiador
- **Screenshot**: `erro_primeira_media_desafiador.png`
- **CSV**: `erro_primeira_media_desafiador.csv`

## Configuração Esperada

### Parâmetros da Cidade Média
- **Faixa de eleitores**: 30.000 a 100.000
- **Média para cálculos**: 65.000 eleitores
- **Teto de gastos**: R$ 115.000

### Cálculos Esperados (Primeira Candidatura)
- **Votos Iniciais**: 0 (primeira candidatura sempre começa do zero)
- **Meta de Votos**: 2% de 65.000 = **1.300 votos**
- **Contatos Iniciais**: 0 (primeira candidatura)
- **Meta de Contatos**: 20% da meta de votos = 20% de 1.300 = **260 contatos**
- **Saldo Inicial**: 10% do teto = 10% de R$ 115.000 = **R$ 11.500**
- **Energia**: 100%
- **Reputação**: 50%

## Resultados Observados

| Parâmetro | Esperado | Observado | Status |
|-----------|----------|-----------|--------|
| Votos Iniciais | 0 | 0 | ✅ OK |
| Meta de Votos | 1.300 | 1.300 | ✅ OK |
| Contatos Iniciais | 0 | 0 | ✅ OK |
| Meta de Contatos | 260 | 260 | ✅ OK |
| Energia | 100% | 100% | ✅ OK |
| Reputação | 50% | 50% | ✅ OK |
| Saldo | R$ 11.500 | **R$ 10.000** | ❌ ERRO |

## Erros Identificados

### 1. Saldo Inicial Incorreto
- **Esperado**: R$ 11.500 (10% de R$ 115.000)
- **Observado**: R$ 10.000
- **Diferença**: -R$ 1.500 (-13%)
- **Gravidade**: **MÉDIA**
- **Impacto**: Jogador tem menos recursos que deveria para cidade média

## Análise

### Observações Importantes

1. **Metas Corretas**: Ao contrário do teste em cidade pequena, as metas de votos e contatos estão **corretas** para cidade média
   - Meta de votos: 1.300 (2% de 65.000) ✅
   - Meta de contatos: 260 (20% de 1.300) ✅

2. **Saldo Fixo Confirmado**: O valor de R$ 10.000 aparece novamente, confirmando que há um valor fixo sendo aplicado independentemente do tamanho da cidade

### Comparação Entre Tamanhos de Cidade

| Cidade | Teto | Saldo Esperado (10%) | Saldo Observado | Diferença |
|--------|------|---------------------|-----------------|-----------|
| Pequena | R$ 35.000 | R$ 3.500 | R$ 10.000 | +R$ 6.500 (+185%) |
| Média | R$ 115.000 | R$ 11.500 | R$ 10.000 | -R$ 1.500 (-13%) |

**Padrão Identificado**: O sistema está usando um valor fixo de R$ 10.000 para todas as configurações, o que:
- **Beneficia** cidades pequenas (dá muito mais dinheiro)
- **Prejudica** cidades médias (dá menos dinheiro)
- Provavelmente **prejudica muito** cidades grandes

### Por Que as Metas Estão Corretas Aqui?

Possíveis explicações:
1. O cálculo de metas pode estar usando valores absolutos corretos para cidade média
2. O erro em cidade pequena pode ser específico daquela configuração
3. Pode haver uma inconsistência no código que calcula metas vs saldo

## Impacto no Gameplay

### Cidade Média vs Cidade Pequena

- **Cidade Pequena**: Jogador tem 2,86x mais dinheiro que deveria (R$ 10k vs R$ 3,5k)
- **Cidade Média**: Jogador tem 13% menos dinheiro que deveria (R$ 10k vs R$ 11,5k)

Isso cria um **desbalanceamento entre tamanhos de cidade**:
- Cidade pequena fica artificialmente mais fácil
- Cidade média fica artificialmente mais difícil
- A progressão de dificuldade não é linear como deveria ser

## Recomendações

### Prioridade ALTA
1. **Eliminar valor fixo de R$ 10.000**
   - Implementar cálculo dinâmico baseado no teto da cidade
   - Fórmula: `saldoInicial = tetoCidade * 0.10` (primeira candidatura)
   - Fórmula: `saldoInicial = tetoCidade * 0.60` (reeleição)

2. **Testar cidade grande**
   - Verificar se o padrão se confirma (teto R$ 500k, esperado R$ 50k, provável R$ 10k)
   - Documentar o impacto em todas as escalas

### Prioridade MÉDIA
3. **Investigar por que as metas estão corretas aqui**
   - Comparar código de cálculo de metas entre cidade pequena e média
   - Entender se há lógica diferente ou se foi coincidência

## Próximos Passos

- Testar Primeira Candidatura em Cidade Grande
- Testar Reeleição em Cidade Média
- Verificar se o erro de metas em cidade pequena é consistente
- Analisar código responsável pelo cálculo de saldo inicial
