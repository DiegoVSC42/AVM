# 🎨 TSX Viewer Pro - Visualizador Universal de Componentes React

O visualizador mais poderoso para testar componentes React/TSX. Suporta **QUALQUER** arquivo TSX com parse completo e mocks automáticos!

## 🚀 Como Usar

### 1. Instalar dependências

```bash
npm install
```

### 2. Iniciar o servidor

```bash
npm run dev
```

O navegador vai abrir automaticamente em `http://localhost:5173`

### 3. Visualizar QUALQUER componente

Simplesmente **cole o arquivo TSX completo** - com imports, exports, tudo!

```tsx
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { trpc } from "@/lib/trpc";
import { useAuth } from "@/_core/hooks/useAuth";

export default function Dashboard() {
  const { user } = useAuth();
  const { data } = trpc.jogo.getEstatisticas.useQuery();
  
  return (
    <div className="p-8">
      <h1>Olá, {user.name}!</h1>
      <Card>
        <p>Estatísticas: {data?.total}</p>
      </Card>
    </div>
  );
}
```

O visualizador vai:
- ✅ **Remover os imports** automaticamente
- ✅ **Fazer parse com Babel** (transpile TSX → JS)
- ✅ **Mockar dependências** (tRPC, hooks, componentes)
- ✅ **Renderizar perfeitamente** em tempo real

## ✨ Funcionalidades Avançadas

### 🎯 Mocks Automáticos

O visualizador já tem mocks prontos para:

- **useAuth()** - Retorna usuário mockado
- **useLocation()** - Hook de navegação
- **trpc** - Queries mockadas com dados de exemplo
- **shadcn/ui** - Card, Button, Dialog, Tooltip, etc
- **Constantes** - CONQUISTAS e outros arrays
- **Lucide Icons** - Todos os ícones disponíveis

### 📦 Componentes Suportados

- ✅ shadcn/ui (Card, Button, Dialog, Tooltip, Alert)
- ✅ Lucide Icons (todos)
- ✅ React Hooks (useState, useEffect, useMemo, etc)
- ✅ Custom Hooks (useAuth, useLocation, etc)
- ✅ tRPC queries
- ✅ Tailwind CSS (todas as classes)

### 🔄 Parse Completo

- ✅ **Babel Transform** - TSX → JS automaticamente
- ✅ **Imports removidos** - Não precisa remover manualmente
- ✅ **TypeScript** - Suporte completo
- ✅ **JSX** - Renderização perfeita

## 🎯 Exemplo de Uso Real

Cole seu componente Dashboard completo:

```tsx
import { Button } from "@/components/ui/button";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { trpc } from "@/lib/trpc";
import { useAuth } from "@/_core/hooks/useAuth";
import { PlayCircle, Trophy, Target } from "lucide-react";

export default function Dashboard() {
  const { user } = useAuth();
  const { data: estatisticas } = trpc.jogo.getEstatisticas.useQuery();
  const { data: partidaAtiva } = trpc.jogo.getPartidaAtiva.useQuery({ 
    jogadorId: "123" 
  });

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-900 via-green-800 to-green-950 p-4">
      <div className="container mx-auto max-w-5xl py-8">
        <h1 className="text-3xl font-bold text-white mb-8">
          Olá, {user.name}!
        </h1>

        {partidaAtiva && (
          <Card className="bg-gradient-to-br from-green-500 to-green-600 mb-6">
            <CardHeader>
              <div className="flex items-center gap-4">
                <PlayCircle className="w-10 h-10 text-white" />
                <div>
                  <CardTitle className="text-white">Continuar Partida</CardTitle>
                  <p className="text-white/90">
                    Fase {partidaAtiva.faseAtual} • {partidaAtiva.decisoesTomadas}/86 decisões
                  </p>
                </div>
              </div>
            </CardHeader>
          </Card>
        )}

        <div className="grid grid-cols-3 gap-4">
          <Card>
            <CardContent className="pt-6">
              <div className="flex items-center gap-2">
                <Target className="w-4 h-4 text-green-400" />
                <div>
                  <p className="text-sm text-gray-500">Partidas</p>
                  <p className="text-2xl font-bold">{estatisticas?.total || 0}</p>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
}
```

**Funciona perfeitamente!** 🎉

## 💡 Dicas

1. **Cole o arquivo completo** - Com imports, exports, tudo
2. **Não precisa remover nada** - O parser faz isso automaticamente
3. **Dados são mockados** - useAuth, trpc, etc retornam dados de exemplo
4. **Hot reload** - Atualiza automaticamente conforme você digita
5. **Teste responsivo** - Alterne entre mobile e desktop

## 🔧 Comandos

```bash
npm run dev      # Inicia servidor de desenvolvimento
npm run build    # Build para produção
npm run preview  # Preview do build de produção
```

## 💡 Dicas

1. **Componentes devem ter export default**: Sempre exporte seu componente principal como `export default`
2. **Imports são automáticos**: React hooks e Lucide icons já estão disponíveis
3. **Use Tailwind**: Todas as classes Tailwind CSS funcionam normalmente
4. **Teste responsividade**: Alterne entre mobile e desktop para testar

## 🐛 Troubleshooting

**Erro: "Component not rendering"**
- Certifique-se que seu componente tem `export default`
- Verifique se não há erros de sintaxe

**Estilos não aplicando**
- Use classes do Tailwind CSS
- Evite CSS inline complexo

**Ícones não aparecem**
- Use ícones do `lucide-react`
- Exemplo: `import { Heart } from 'lucide-react'`

## 📝 Licença

MIT

---

**Feito com ❤️ para facilitar o desenvolvimento React**
