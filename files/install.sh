#!/bin/bash

# Script de instalação rápida do Live Tailwind Editor
# Execute na raiz do seu projeto: bash install-live-editor.sh

echo "🎨 Instalando Live Tailwind Editor..."

# Cria estrutura de pastas se não existir
mkdir -p client/src/components
mkdir -p client/src/hooks

# Copia arquivos
echo "📦 Copiando componentes..."
cp live-tailwind-editor/components/LiveTailwindEditor.tsx client/src/components/
cp live-tailwind-editor/hooks/useDevTools.ts client/src/hooks/
cp live-tailwind-editor/DevToolsWrapper.tsx client/src/

# Cria página de demo (opcional)
read -p "Deseja instalar a página de demo? (s/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Ss]$ ]]
then
    mkdir -p client/src/pages
    cp live-tailwind-editor/demo/LiveEditorDemo.tsx client/src/pages/
    echo "✅ Página de demo instalada em client/src/pages/LiveEditorDemo.tsx"
fi

echo ""
echo "✅ Instalação concluída!"
echo ""
echo "📝 Próximos passos:"
echo ""
echo "1. Adicione no seu App.tsx:"
echo ""
echo "   import { DevToolsWrapper } from './DevToolsWrapper';"
echo ""
echo "   function App() {"
echo "     return ("
echo "       <DevToolsWrapper>"
echo "         {/* Seu código existente */}"
echo "       </DevToolsWrapper>"
echo "     );"
echo "   }"
echo ""
echo "2. Execute o projeto:"
echo ""
echo "   pnpm dev"
echo ""
echo "3. Pressione Ctrl + Shift + E para abrir o editor!"
echo ""
echo "📚 Documentação completa: live-tailwind-editor/docs/LIVE_EDITOR_GUIDE.md"
