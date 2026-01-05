import React from 'react';
import { Card } from '@/components/ui/card';
import { Button } from '@/components/ui/button';

/**
 * Página de exemplo para testar o Live Tailwind Editor
 * 
 * Como usar:
 * 1. Pressione Ctrl + Shift + E para abrir o editor
 * 2. Clique em "Inspecionar Elemento"
 * 3. Clique em qualquer elemento desta página
 * 4. Ajuste as classes Tailwind
 * 5. Clique em "Aplicar" para ver as mudanças
 * 6. Copie o código atualizado
 */
export const LiveEditorDemo: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-50 p-8">
      {/* Header */}
      <div className="max-w-4xl mx-auto mb-8">
        <h1 className="text-4xl font-bold text-gray-900 mb-2">
          Live Tailwind Editor Demo
        </h1>
        <p className="text-gray-600">
          Pressione <kbd className="px-2 py-1 bg-gray-200 rounded text-sm font-mono">Ctrl + Shift + E</kbd> para começar
        </p>
      </div>

      {/* Grid de exemplos */}
      <div className="max-w-4xl mx-auto grid gap-6">
        
        {/* Card 1 - Hero Section */}
        <Card className="p-8 bg-gradient-to-r from-blue-500 to-purple-600">
          <div className="text-center text-white">
            <h2 className="text-3xl font-bold mb-4">
              Experimente Editar Este Card
            </h2>
            <p className="text-lg mb-6 text-blue-100">
              Clique neste card no modo de inspeção e ajuste:
              <br />
              • Padding (p-8)
              <br />
              • Cores do gradiente
              <br />
              • Tamanho do texto
            </p>
            <Button className="bg-white text-blue-600 hover:bg-blue-50">
              Botão de Ação
            </Button>
          </div>
        </Card>

        {/* Card 2 - Features Grid */}
        <Card className="p-6">
          <h3 className="text-2xl font-bold mb-4 text-gray-900">
            Recursos para Testar
          </h3>
          <div className="grid grid-cols-3 gap-4">
            <div className="p-4 bg-blue-50 rounded-lg">
              <div className="w-12 h-12 bg-blue-500 rounded-full mb-3"></div>
              <h4 className="font-semibold mb-2">Feature 1</h4>
              <p className="text-sm text-gray-600">
                Ajuste o padding desta caixa
              </p>
            </div>
            
            <div className="p-4 bg-green-50 rounded-lg">
              <div className="w-12 h-12 bg-green-500 rounded-full mb-3"></div>
              <h4 className="font-semibold mb-2">Feature 2</h4>
              <p className="text-sm text-gray-600">
                Mude as cores de fundo
              </p>
            </div>
            
            <div className="p-4 bg-purple-50 rounded-lg">
              <div className="w-12 h-12 bg-purple-500 rounded-full mb-3"></div>
              <h4 className="font-semibold mb-2">Feature 3</h4>
              <p className="text-sm text-gray-600">
                Teste diferentes gaps
              </p>
            </div>
          </div>
        </Card>

        {/* Card 3 - Form Example */}
        <Card className="p-6">
          <h3 className="text-xl font-bold mb-4">
            Exemplo de Formulário
          </h3>
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium mb-2">
                Nome Completo
              </label>
              <input
                type="text"
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                placeholder="Digite seu nome"
              />
            </div>
            
            <div>
              <label className="block text-sm font-medium mb-2">
                Email
              </label>
              <input
                type="email"
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                placeholder="seu@email.com"
              />
            </div>
            
            <div className="flex gap-3">
              <Button className="flex-1 bg-blue-600 hover:bg-blue-700">
                Enviar
              </Button>
              <Button variant="outline" className="flex-1">
                Cancelar
              </Button>
            </div>
          </div>
        </Card>

        {/* Card 4 - Stats */}
        <div className="grid grid-cols-3 gap-4">
          <Card className="p-6 text-center">
            <div className="text-4xl font-bold text-blue-600 mb-2">
              2.5K
            </div>
            <div className="text-sm text-gray-600">
              Usuários Ativos
            </div>
          </Card>
          
          <Card className="p-6 text-center">
            <div className="text-4xl font-bold text-green-600 mb-2">
              98%
            </div>
            <div className="text-sm text-gray-600">
              Satisfação
            </div>
          </Card>
          
          <Card className="p-6 text-center">
            <div className="text-4xl font-bold text-purple-600 mb-2">
              24/7
            </div>
            <div className="text-sm text-gray-600">
              Suporte
            </div>
          </Card>
        </div>

        {/* Card 5 - Buttons Showcase */}
        <Card className="p-6">
          <h3 className="text-xl font-bold mb-4">
            Galeria de Botões
          </h3>
          <div className="flex flex-wrap gap-3">
            <Button className="bg-blue-600">
              Primary
            </Button>
            <Button variant="outline">
              Outline
            </Button>
            <Button className="bg-green-600">
              Success
            </Button>
            <Button className="bg-red-600">
              Danger
            </Button>
            <Button className="bg-yellow-500 text-black">
              Warning
            </Button>
            <Button variant="ghost">
              Ghost
            </Button>
          </div>
        </Card>

        {/* Card 6 - Complex Layout */}
        <Card className="p-6">
          <div className="flex gap-6">
            <div className="flex-1">
              <img
                src="https://via.placeholder.com/400x300"
                alt="Placeholder"
                className="w-full rounded-lg mb-4"
              />
              <h3 className="text-xl font-bold mb-2">
                Layout Complexo
              </h3>
              <p className="text-gray-600 mb-4">
                Este é um exemplo de layout mais complexo com imagem, texto e botões.
                Experimente ajustar os espaçamentos e alinhamentos.
              </p>
              <div className="flex gap-2">
                <Button size="sm" className="bg-blue-600">
                  Ler Mais
                </Button>
                <Button size="sm" variant="outline">
                  Compartilhar
                </Button>
              </div>
            </div>
            
            <div className="w-64 space-y-4">
              <div className="p-4 bg-gray-50 rounded-lg">
                <h4 className="font-semibold mb-2">Info Box 1</h4>
                <p className="text-sm text-gray-600">
                  Informação adicional aqui
                </p>
              </div>
              <div className="p-4 bg-blue-50 rounded-lg">
                <h4 className="font-semibold mb-2">Info Box 2</h4>
                <p className="text-sm text-gray-600">
                  Mais conteúdo relevante
                </p>
              </div>
            </div>
          </div>
        </Card>

        {/* Instructions */}
        <Card className="p-6 bg-yellow-50 border-yellow-200">
          <h3 className="text-xl font-bold mb-3 text-yellow-900">
            📋 Instruções de Uso
          </h3>
          <ol className="space-y-2 text-sm text-yellow-800">
            <li>
              <strong>1.</strong> Pressione <kbd className="px-2 py-1 bg-yellow-200 rounded">Ctrl + Shift + E</kbd> para abrir o editor
            </li>
            <li>
              <strong>2.</strong> Clique em "Inspecionar Elemento"
            </li>
            <li>
              <strong>3.</strong> Clique em qualquer elemento desta página
            </li>
            <li>
              <strong>4.</strong> Use a aba "Visual" para ajustes rápidos ou "Código" para edição manual
            </li>
            <li>
              <strong>5.</strong> Clique em "Aplicar" para ver as mudanças
            </li>
            <li>
              <strong>6.</strong> Clique no ícone de cópia para copiar o código atualizado
            </li>
            <li>
              <strong>7.</strong> Cole o código no seu arquivo .tsx
            </li>
          </ol>
        </Card>
      </div>
    </div>
  );
};
