# Auditoria: Teste "Discordar Totalmente"

Realizei a verificação do cálculo ideológico utilizando a estratégia de selecionar **"Discordar Totalmente"** em todas as 10 questões.

## Resumo Comparativo

| Dimensão | Esperado (Lógica Correta*) | Obtido na UI | Discrepância |
| :--- | :--- | :--- | :--- |
| **Social (Prog)** | **0%** | 50% | +50% |
| **Liberal** | **33%** | 17% | -16% |
| **Conservador** | **67%** | 33% | -34% |

*\*A lógica correta deve considerar apenas saldos positivos, ignorando dimensões com pontuação negativa.*

## Memória de Cálculo (Esperado)

De acordo com `Valores.csv`, ao discordar totalmente de tudo, os saldos finais acumulados são:

*   **Social**: -1 (Como é negativo, considera-se **0**)
*   **Liberal**: 1
*   **Conservador**: 2

**Cálculo das Porcentagens**:
*   Soma Total (apenas positivos): 0 + 1 + 2 = **3**
*   **Social**: 0 / 3 = **0%**
*   **Liberal**: 1 / 3 = 33.3% -> **33%**
*   **Conservador**: 2 / 3 = 66.6% -> **67%**


> **Inconsistência Crítica**: A interface atual exibe um perfil predominantemente Social (50%), enquanto a lógica de cálculo correta (baseada nos valores do CSV e ignorando negativos) deveria resultar em um perfil majoritariamente **Conservador (67%)**.

## Arquivos Gerados
- **Rastreamento Detalhado**: [verificacao_discordar.csv](file:///d:/GIT/AVM/Testes%20Jogo%20Eu%20vereador/Perfil-Ideologico/verificacao_discordar.csv)
- **Captura do Resultado**: ![Resultado UI](file:///C:/Users/Admin/.gemini/antigravity/brain/56eacd6c-98d4-452f-8be0-b9e9a90ad3cb/quiz_final_results_1767970012081.png)
