# Solicitações de Ajustes e Melhorias - 09/01/2026

Este documento organiza as demandas em duas seções principais: feedbacks de bugs encontrados e solicitações de novas funcionalidades/ajustes.

---

## Seção 1: Feedback de Problemas (Versão Atual)

### 1.1. Erro na Biografia (DNA)
**Problema:** Ao editar a Biografia (DNA), a mensagem de conclusão aparece, mas ao retornar para a dashboard, o status não consta como completo.

<div style="page-break-inside: avoid;">
<strong>Evidências:</strong>
<p align="center"><img src="images/image.png" alt="Erro Dashboard" width="50%"></p>
<p align="center"><img src="images/image%201.png" alt="Erro Status" width="75%"></p>
</div>

### 1.2. Salvamento Automático de Rascunhos
**Problema:** Atualmente, os rascunhos são salvos apenas quando o usuário clica no botão "Salvar Rascunho".

**Melhoria Solicitada:** Implementar o salvamento automático do rascunho sempre que o usuário:
- Sair da tela de preenchimento.
- Fechar a janela ou aba do navegador.
- Navegar para outra área do sistema.

**Objetivo:** Evitar perda de progresso caso o usuário saia acidentalmente ou esqueça de salvar manualmente.

### 1.3. Confirmação de Exclusão de Rascunho
**Problema:** Ao excluir um rascunho na dashboard, a ação é executada imediatamente sem confirmação prévia, e apenas uma notificação de desfazer aparece.

**Melhoria Solicitada:**
1.  **Modal/Alerta de Confirmação:** Antes de excluir, exibir um pedido de confirmação (ex: "Tem certeza que deseja excluir este rascunho?").
2.  **Notificação de Desfazer:** Manter a opção de "Desfazer" (Undo) após a confirmação e exclusão, como uma camada extra de segurança.

**Objetivo:** Prevenir exclusões acidentais de conteúdo importante.

### 1.4. Inconsistência no Status de Renovação (Plano Cancelado)
**Problema:** Mesmo após o usuário cancelar a assinatura (confirmado na tela de detalhes), a dashboard principal ainda exibe a mensagem "Renova em 06/02/2026", o que confunde o usuário.

<div style="page-break-inside: avoid;">
<strong>Estado Correto (Tela de Assinatura):</strong>
<p align="center"><img src="images/assinatura_cancelada.png" alt="Assinatura Cancelada" width="50%"></p>
</div>

<div style="page-break-inside: avoid;">
<strong>Estado Incorreto (Dashboard):</strong>
<p align="center"><img src="images/dashboard_renova_erro.png" alt="Erro Dashboard Renova" width="75%"></p>
</div>

### 1.5. Delay no Carregamento de Dados do Usuário (Tela de Perfil)
**Problema:** Ao acessar a tela de Perfil, o sistema exibe inicialmente um estado genérico ("Usuário" e "Sem e-mail") e demora alguns instantes para carregar os dados reais do usuário.

<div style="page-break-inside: avoid;">
<strong>Estado Inicial (Carregando):</strong>
<p align="center"><img src="images/profile_loading_delay_1.png" alt="Carregando Dados" width="50%"></p>
</div>

<div style="page-break-inside: avoid;">
<strong>Estado Final (Carregado):</strong>
<p align="center"><img src="images/profile_loading_delay_2.png" alt="Dados Carregados" width="50%"></p>
</div>



---

## Seção 2: Adições e Melhorias (Novas Implementações)

### 2.1. Alteração no Sistema de Canais
**Objetivo:** Alterar a representação dos canais para alinhar com a lógica dos agentes.

<div style="page-break-inside: avoid;">
<strong>Referência Visual (Como deve ficar):</strong>
<p align="center"><img src="images/image%203.png" alt="Novo Layout Canais 1" width="50%"></p>
<p align="center"><img src="images/image%204.png" alt="Novo Layout Canais 2" width="50%"></p>
</div>

**Estrutura de Dados:**
A estrutura deve seguir rigorosamente o arquivo `canais.json`.

Exemplo da estrutura esperada:
```json
"Instagram": {
    "formatos": [
        "Reels",
        "Stories",
        "Card/Foto",
        "Carrossel"
    ]
}
```

### 2.2. Modal de Explicação em "Ato de Mandato"
**Objetivo:** Adicionar um modal explicativo na tela do formulário de Ato de Mandato para auxiliar o usuário. O modal deve ter um botão de acesso e conter as seções:
- **O que é**
- **Contexto e importância**
- **Exemplos práticos**

<div style="page-break-inside: avoid;">
<strong>Referência Visual (Sugestão de Layout):</strong>
<p align="center"><img src="images/modal_explicacao_mobilizacao.png" alt="Modal de Explicação" width="50%"></p>
</div>

### 2.3. Atualização dos Formulários de Ato de Mandato
**Objetivo:** Atualizar os formulários e placeholders para conformidade total com o arquivo `atos_de_mandato.json`.

**Detalhes da Implementação:**
O arquivo JSON contém a "verdade" para cada tipo de ato (Mobilização, Reunião, etc.):
1.  **Textos do Modal:** Usar os dados da chave `explicacao` (definicao, contexto_e_importancia, exemplos_praticos).
2.  **Campos do Formulário:** Usar a lista em `perguntas` para gerar os inputs.

**Nota:** Garantir que todos os formulários da aplicação estejam sincronizados com este JSON.

