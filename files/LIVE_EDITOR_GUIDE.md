# Live Tailwind Editor - Guia de Instalação e Uso

## 📦 Instalação

### 1. Copie os arquivos para o projeto

Copie os seguintes arquivos para suas respectivas pastas:

```
client/src/
├── components/
│   └── LiveTailwindEditor.tsx    # Componente principal
├── hooks/
│   └── useDevTools.ts             # Hook de controle
└── DevToolsWrapper.tsx            # Wrapper para o app
```

### 2. Integre no seu App.tsx

```tsx
// client/src/App.tsx
import { DevToolsWrapper } from './DevToolsWrapper';

function App() {
  return (
    <DevToolsWrapper>
      {/* Seu app existente */}
      <Router>
        {/* ... suas rotas ... */}
      </Router>
    </DevToolsWrapper>
  );
}

export default App;
```

## 🎯 Como Usar

### Abrir o Editor

- **Atalho de teclado**: `Ctrl + Shift + E`
- **Fechar**: `Escape` ou clique no botão de fechar

### Modo de Inspeção

1. Clique em **"Inspecionar Elemento"**
2. Clique em qualquer elemento da página
3. O editor mostrará as classes Tailwind do elemento

### Aba Visual

Ajuste propriedades com controles visuais:

#### Espaçamento
- **Padding**: Arraste o slider para ajustar `p-0` até `p-32`
- **Margin**: Arraste o slider para ajustar `m-0` até `m-32`
- **Gap**: Arraste o slider para ajustar `gap-0` até `gap-32`

#### Tamanho
- Clique nos botões para aplicar: `w-full`, `w-1/2`, `w-1/3`, `w-auto`

#### Cores
- Clique nos quadrados coloridos para mudar cor de fundo
- Opções: branco, cinza, azul, verde, vermelho

### Aba Código

Edite diretamente as classes Tailwind:

```tsx
// Antes
<div className="p-4 bg-white">

// Edite para
<div className="p-8 bg-blue-500 rounded-lg shadow-xl">
```

### Aplicar Mudanças

1. Ajuste as classes (visual ou código)
2. Clique em **"Aplicar"**
3. As mudanças aparecem instantaneamente na página

### Copiar Código

1. Clique no botão de **cópia** (ícone de copy)
2. Cole o código no seu arquivo `.tsx`

Exemplo do que é copiado:
```tsx
<div className="p-8 m-4 bg-blue-500 text-white rounded-lg">
  {/* Conteúdo */}
</div>
```

### Desfazer (Undo)

- Clique no botão **↻** para desfazer última mudança
- Histórico completo de alterações

### Exportar Mudanças

1. Clique em **"Exportar Mudanças"**
2. Baixa um arquivo JSON com todas as alterações
3. Use para documentar ou compartilhar mudanças

Formato do arquivo:
```json
[
  {
    "path": "div.container > button.btn-primary",
    "oldClasses": "p-4 bg-blue-500",
    "newClasses": "p-8 bg-blue-600 rounded-lg"
  }
]
```

## 🎨 Fluxo de Trabalho Recomendado

### Para ajustes rápidos:

1. `Ctrl + Shift + E` - Abre o editor
2. Clique em "Inspecionar Elemento"
3. Clique no elemento que quer editar
4. Use a aba **Visual** para ajustes rápidos
5. Clique em "Aplicar"
6. Clique no botão de copiar
7. Cole no arquivo `.tsx`

### Para ajustes complexos:

1. `Ctrl + Shift + E` - Abre o editor
2. Clique em "Inspecionar Elemento"
3. Clique no elemento
4. Vá para aba **Código**
5. Edite as classes manualmente
6. Clique em "Aplicar" para testar
7. Quando estiver satisfeito, copie o código

### Para múltiplas mudanças:

1. Faça todas as alterações que precisa
2. Teste visualmente na página
3. Clique em "Exportar Mudanças"
4. Use o JSON como referência para atualizar seus arquivos

## 💡 Dicas e Truques

### Atalhos de Teclado

- `Ctrl + Shift + E` - Abrir/fechar editor
- `Escape` - Fechar editor
- `Ctrl + Z` (funcionalidade futura) - Desfazer

### Classes Comuns

#### Layout
```
flex, flex-col, flex-row, grid, grid-cols-2, grid-cols-3
items-center, justify-center, justify-between
```

#### Espaçamento
```
p-4, p-8, px-6, py-4, m-4, mx-auto, gap-4
```

#### Tamanho
```
w-full, w-1/2, h-full, h-screen, max-w-lg
```

#### Cores
```
bg-blue-500, text-white, border-gray-300
hover:bg-blue-600, focus:ring-2
```

#### Visual
```
rounded, rounded-lg, shadow, shadow-xl
border, border-2, opacity-50
```

### Workflow com Manus

1. **Peça ao Manus** para criar o componente inicial
2. **Use o editor** para ajustes visuais finos
3. **Copie o código** atualizado
4. **Cole de volta** no chat do Manus com:
   ```
   "Atualize o componente X com estas classes:
   className="p-8 bg-blue-500 rounded-lg shadow-xl"
   ```

Isso economiza créditos evitando iterações de ajuste visual!

## 🔧 Personalização

### Adicionar mais cores

Edite `LiveTailwindEditor.tsx`, linha ~350:

```tsx
{['bg-white', 'bg-gray-100', 'bg-blue-500', 'bg-purple-500', 'bg-pink-500'].map(bg => (
  // ...
))}
```

### Adicionar mais tamanhos

Linha ~330:

```tsx
{['w-full', 'w-1/2', 'w-1/3', 'w-1/4', 'w-auto'].map(w => (
  // ...
))}
```

### Mudar atalho de teclado

Edite `useDevTools.ts`, linha ~8:

```tsx
// De: Ctrl + Shift + E
if (e.ctrlKey && e.shiftKey && e.key === 'E')

// Para: Ctrl + Alt + D
if (e.ctrlKey && e.altKey && e.key === 'D')
```

## 🐛 Troubleshooting

### Editor não aparece

- Verifique se está em modo de desenvolvimento (`npm run dev`)
- Verifique se o `DevToolsWrapper` está no `App.tsx`
- Veja o console do navegador para erros

### Classes não aplicam

- Certifique-se que são classes Tailwind válidas
- Verifique se o Tailwind está configurado corretamente
- Algumas classes dinâmicas podem não funcionar (ex: `bg-[#123456]`)

### Elemento não seleciona

- Tente clicar novamente no modo de inspeção
- Alguns elementos podem estar cobertos por outros
- Use o DevTools do navegador (F12) como alternativa

## 📊 Comparação de Custo

### Antes (com Manus):
```
Você: "Aumenta o padding desse botão"
Manus: [10-50 créditos] ✅

Você: "Agora deixa azul mais escuro"
Manus: [10-50 créditos] ✅

Você: "Adiciona sombra"
Manus: [10-50 créditos] ✅

Total: 30-150 créditos para 3 ajustes
```

### Depois (com Live Editor):
```
Você: [abre editor, ajusta, copia código]
Manus: 0 créditos ✅

Você: "Atualize o botão com: className='p-6 bg-blue-600 shadow-xl'"
Manus: [5-10 créditos] ✅

Total: 5-10 créditos para 3+ ajustes
```

**Economia: ~70-90% em ajustes visuais!** 🎉

## 🚀 Próximos Passos

Sugestões de melhorias:

1. [ ] Adicionar histórico persistente (localStorage)
2. [ ] Suporte para classes responsivas (`md:`, `lg:`)
3. [ ] Preview side-by-side
4. [ ] Integração com Figma
5. [ ] Biblioteca de componentes salvos
6. [ ] Modo colaborativo

## 📝 Licença

Livre para usar e modificar!
