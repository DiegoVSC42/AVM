# 🎨 Live Tailwind Editor

Edite visualmente as classes Tailwind dos seus componentes **sem gastar créditos do Manus**!

## ⚡ Quick Start (3 passos)

### 1. Copie os arquivos

```bash
# Estrutura de pastas
client/src/
├── components/
│   └── LiveTailwindEditor.tsx
├── hooks/
│   └── useDevTools.ts
└── DevToolsWrapper.tsx
```

### 2. Adicione no App.tsx

```tsx
import { DevToolsWrapper } from './DevToolsWrapper';

function App() {
  return (
    <DevToolsWrapper>
      {/* Seu código existente */}
    </DevToolsWrapper>
  );
}
```

### 3. Use!

```
Pressione: Ctrl + Shift + E
```

## 🎯 Como Usar

1. **Abra o editor**: `Ctrl + Shift + E`
2. **Clique em "Inspecionar Elemento"**
3. **Clique no elemento** que quer editar
4. **Ajuste as classes** (visual ou código)
5. **Clique em "Aplicar"**
6. **Copie o código** (botão de copiar)
7. **Cole no seu .tsx**

## 💰 Economia de Créditos

### ❌ Antes (só com Manus)
```
Você: "Aumenta o padding"        [30 créditos]
Você: "Agora mais azul"           [30 créditos]
Você: "Adiciona sombra"           [30 créditos]
───────────────────────────────────────────────
Total: 90 créditos
```

### ✅ Depois (com Live Editor)
```
Você: [ajusta visualmente]        [0 créditos]
Você: [copia e cola no Manus]     [5 créditos]
───────────────────────────────────────────────
Total: 5 créditos (94% de economia!)
```

## 🎨 Recursos

### Aba Visual
- ✅ **Sliders** para padding, margin, gap
- ✅ **Botões** para tamanhos (w-full, w-1/2, etc)
- ✅ **Paleta de cores** para background
- ✅ **Preview em tempo real**

### Aba Código
- ✅ Editor de texto para classes
- ✅ Autocomplete do Tailwind
- ✅ Visualização lado a lado

### Funcionalidades
- ✅ Histórico de alterações (Ctrl+Z)
- ✅ Exportar mudanças (.json)
- ✅ Copiar código para clipboard
- ✅ Inspeção hover (passa o mouse)
- ✅ Minimizar editor

## 📱 Atalhos

| Atalho | Ação |
|--------|------|
| `Ctrl + Shift + E` | Abrir/fechar editor |
| `Escape` | Fechar editor |
| `↻` (botão) | Desfazer última mudança |

## 🔥 Exemplo Real

**Antes** (3 iterações com Manus):
```tsx
<button className="p-4 bg-blue-500">
  Clique
</button>
```

**Depois** (1 ajuste manual):
```tsx
<button className="px-8 py-4 bg-blue-600 hover:bg-blue-700 rounded-xl shadow-lg transform hover:scale-105 transition-all">
  Clique
</button>
```

## 🎓 Workflow Recomendado

1. **Peça ao Manus** criar componente base
   ```
   "Crie um card de produto com imagem, título e preço"
   ```

2. **Use o Live Editor** para ajustes finos
   - Espaçamentos
   - Cores
   - Tamanhos
   - Sombras

3. **Copie o resultado** e cole de volta
   ```
   "Atualize o card com estas classes:
   className='p-6 bg-white rounded-2xl shadow-xl hover:shadow-2xl'"
   ```

4. **Economize 70-90%** dos créditos! 🎉

## 🐛 Troubleshooting

**Editor não aparece?**
- Certifique-se que está em modo dev (`npm run dev`)
- Verifique se `DevToolsWrapper` está no `App.tsx`

**Classes não aplicam?**
- Verifique se são classes Tailwind válidas
- Algumas classes dinâmicas podem não funcionar

**Elemento não seleciona?**
- Clique novamente no modo de inspeção
- Use DevTools do navegador (F12) como alternativa

## 📚 Documentação Completa

Veja `LIVE_EDITOR_GUIDE.md` para:
- Tutorial detalhado
- Personalização
- Classes comuns
- Exemplos avançados

## 🎮 Página de Demo

Quer testar? Use o componente `LiveEditorDemo.tsx`:

```tsx
import { LiveEditorDemo } from './LiveEditorDemo';

// Em qualquer rota
<Route path="/demo" component={LiveEditorDemo} />
```

## 🚀 Features Futuras

- [ ] Suporte para classes responsivas (`md:`, `lg:`)
- [ ] Biblioteca de componentes salvos
- [ ] Preview side-by-side
- [ ] Integração com Figma
- [ ] Modo dark

## 📄 Licença

MIT - Use e abuse! 🎨

---

**Economize créditos e ajuste layouts 10x mais rápido!** ⚡
