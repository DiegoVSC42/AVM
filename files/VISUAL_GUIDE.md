# 🎨 Live Tailwind Editor - Guia Visual

```
┌─────────────────────────────────────────────────────────────┐
│                    SEU COMPONENTE                           │
│  ┌─────────────────────────────────────────────────┐        │
│  │                                                 │        │
│  │   <div className="p-4 bg-blue-500">            │        │
│  │      Olá Mundo                                  │        │
│  │   </div>                                        │        │
│  │                                                 │        │
│  └─────────────────────────────────────────────────┘        │
│                                                             │
│  Pressione: Ctrl + Shift + E                               │
│                                                             │
│                          ↓                                  │
│                                                             │
│  ┌──────────────────────────────────────────────┐          │
│  │ 🎨 Live Tailwind Editor            _ □ ✕    │          │
│  ├──────────────────────────────────────────────┤          │
│  │                                              │          │
│  │  [🔍 Inspecionar Elemento]                  │          │
│  │                                              │          │
│  │  Elemento Selecionado:                       │          │
│  │  div.container > div                         │          │
│  │                                              │          │
│  │  ┌─ Visual ─┬─ Código ─┐                   │          │
│  │  │                      │                   │          │
│  │  │  Espaçamento:        │                   │          │
│  │  │  Padding: [====] 4   │                   │          │
│  │  │  Margin:  [==  ] 2   │                   │          │
│  │  │  Gap:     [    ] 0   │                   │          │
│  │  │                      │                   │          │
│  │  │  Largura:            │                   │          │
│  │  │  [full][1/2][1/3][auto]                 │          │
│  │  │                      │                   │          │
│  │  │  Cor de Fundo:       │                   │          │
│  │  │  [⬜][⬜][🟦][🟩][🟥]  │                   │          │
│  │  │                      │                   │          │
│  │  └──────────────────────┘                   │          │
│  │                                              │          │
│  │  [💾 Aplicar] [📋 Copiar] [↻ Desfazer]     │          │
│  │                                              │          │
│  └──────────────────────────────────────────────┘          │
│                                                             │
│                          ↓                                  │
│                                                             │
│  ┌─────────────────────────────────────────────────┐        │
│  │ RESULTADO INSTANTÂNEO                          │        │
│  │                                                 │        │
│  │   <div className="p-8 m-2 bg-blue-600">       │        │
│  │      Olá Mundo                                 │        │
│  │   </div>                                       │        │
│  │                                                 │        │
│  └─────────────────────────────────────────────────┘        │
│                                                             │
│  Clique em [📋 Copiar] para copiar o código!              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 🚀 Fluxo de Trabalho

```
ANTES (Com Manus):
┌──────────────────────────────────────────────┐
│ Você: "Aumenta o padding desse botão"      │ → 💰 30 créditos
├──────────────────────────────────────────────┤
│ Manus: [gera código]                        │
└──────────────────────────────────────────────┘
          ↓
┌──────────────────────────────────────────────┐
│ Você: "Agora deixa azul mais escuro"       │ → 💰 30 créditos
├──────────────────────────────────────────────┤
│ Manus: [gera código]                        │
└──────────────────────────────────────────────┘
          ↓
┌──────────────────────────────────────────────┐
│ Você: "Adiciona sombra e arredonda"        │ → 💰 30 créditos
├──────────────────────────────────────────────┤
│ Manus: [gera código]                        │
└──────────────────────────────────────────────┘
                                        Total: 💰 90 créditos


DEPOIS (Com Live Editor):
┌──────────────────────────────────────────────┐
│ Você: [abre editor com Ctrl+Shift+E]       │ → ✅ 0 créditos
│       [ajusta visualmente]                  │
│       [copia código]                        │
├──────────────────────────────────────────────┤
│ Live Editor: [mudanças instantâneas]        │
└──────────────────────────────────────────────┘
          ↓
┌──────────────────────────────────────────────┐
│ Você: "Atualiza o botão com essas classes" │ → 💰 5 créditos
├──────────────────────────────────────────────┤
│ Manus: [atualiza arquivo]                  │
└──────────────────────────────────────────────┘
                                        Total: 💰 5 créditos
                                     Economia: 94% 🎉
```

## 📊 Comparação Visual

```
┌─────────────────────────┬──────────────────────────┐
│   SEM Live Editor       │   COM Live Editor        │
├─────────────────────────┼──────────────────────────┤
│                         │                          │
│  Você → Manus           │  Você → Live Editor      │
│    ↓                    │    ↓                     │
│  Manus gera código      │  Ajuste visual           │
│    ↓                    │    ↓                     │
│  Você pede mudança      │  Copia código            │
│    ↓                    │    ↓                     │
│  Manus gera código      │  Manus atualiza          │
│    ↓                    │    ✓                     │
│  Você pede mudança      │                          │
│    ↓                    │                          │
│  Manus gera código      │                          │
│    ✓                    │                          │
│                         │                          │
│  ⏱️  Tempo: 5-10 min    │  ⏱️  Tempo: 1-2 min      │
│  💰 Custo: 90 créditos  │  💰 Custo: 5 créditos    │
│  🔄 Iterações: 3+       │  🔄 Iterações: 1         │
│                         │                          │
└─────────────────────────┴──────────────────────────┘
```

## 🎯 Casos de Uso

```
✅ PERFEITO PARA:
────────────────
│ • Ajustar espaçamentos (padding, margin, gap)
│ • Trocar cores de fundo e texto
│ • Mudar tamanhos (width, height)
│ • Testar diferentes layouts
│ • Ajustes finos de UI
│ • Prototipar rapidamente
└────────────────

❌ NÃO IDEAL PARA:
──────────────────
│ • Criar componentes do zero (use Manus)
│ • Lógica complexa (use Manus)
│ • Estrutura de dados (use Manus)
│ • Refatoração grande (use Manus)
└──────────────────

💡 MELHOR COMBINAÇÃO:
─────────────────────
│ 1. Manus cria a estrutura base
│ 2. Live Editor para ajustes visuais
│ 3. Manus para features complexas
│ 4. Live Editor para polish final
└─────────────────────
```

## 🎮 Atalhos de Teclado

```
┌──────────────────────────────────────────┐
│  Ctrl + Shift + E  →  Abrir/Fechar      │
│  Escape            →  Fechar             │
│  Clique + Arraste  →  Ajustar sliders    │
│  Ctrl + C          →  Copiar (futuro)    │
│  Ctrl + Z          →  Desfazer (futuro)  │
└──────────────────────────────────────────┘
```

## 📈 Produtividade

```
Tarefa: Criar e ajustar um card de produto

SEM Live Editor:
─────────────────
Passo 1: "Cria um card"                    [2 min]  [30 créditos]
Passo 2: "Aumenta o padding"               [1 min]  [20 créditos]
Passo 3: "Muda cor para azul escuro"       [1 min]  [20 créditos]
Passo 4: "Adiciona sombra"                 [1 min]  [20 créditos]
Passo 5: "Arredonda os cantos"             [1 min]  [20 créditos]
Passo 6: "Adiciona hover effect"           [1 min]  [20 créditos]
─────────────────────────────────────────────────────────────
Total:                                      [7 min]  [130 créditos]


COM Live Editor:
────────────────
Passo 1: "Cria um card base"               [2 min]  [30 créditos]
Passo 2: [Ctrl+Shift+E, ajusta tudo]       [2 min]  [0 créditos]
Passo 3: "Atualiza com essas classes"      [1 min]  [5 créditos]
─────────────────────────────────────────────────────────────
Total:                                      [5 min]  [35 créditos]

ECONOMIA: 2 minutos + 95 créditos (73%) 🚀
```

## 🔧 Instalação Rápida

```bash
# 1. Execute o script de instalação
bash install.sh

# 2. Adicione no App.tsx
# Veja README.md para detalhes

# 3. Inicie o projeto
pnpm dev

# 4. Pressione Ctrl + Shift + E
# 🎉 Pronto para usar!
```

## 💡 Dica de Ouro

```
┌────────────────────────────────────────────────┐
│                                                │
│  Use Manus para CRIAR                         │
│  Use Live Editor para AJUSTAR                 │
│                                                │
│  Essa combinação é IMPARÁVEL! 🚀              │
│                                                │
└────────────────────────────────────────────────┘
```
