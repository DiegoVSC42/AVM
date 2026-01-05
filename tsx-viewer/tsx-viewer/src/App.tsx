import { useState, useEffect, useRef } from 'react';
import { Upload, Eye, Code, Smartphone, Monitor, AlertCircle, Loader2, CheckCircle } from 'lucide-react';
// @ts-ignore
import * as Babel from '@babel/standalone';

const DEFAULT_COMPONENT = `export default function ExemploComponente() {
  const [count, setCount] = useState(0);
  
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-900 via-blue-800 to-blue-950 p-4">
      <div className="container mx-auto max-w-4xl py-8">
        <h1 className="text-4xl font-bold text-white mb-4">
          TSX Viewer Pro! 👋
        </h1>
        <p className="text-blue-200 text-lg mb-6">
          Cole seu código completo aqui ao lado!
        </p>
        
        <div className="bg-white/10 backdrop-blur border border-white/20 rounded-lg p-6">
          <h2 className="text-2xl font-semibold text-white mb-3">
            Contador: {count}
          </h2>
          <button 
            onClick={() => setCount(count + 1)}
            className="bg-green-500 hover:bg-green-600 text-white px-6 py-2 rounded-lg font-bold"
          >
            Incrementar
          </button>
        </div>
      </div>
    </div>
  );
}`;

function App() {
  const [code, setCode] = useState(DEFAULT_COMPONENT);
  const [viewMode, setViewMode] = useState<'desktop' | 'mobile'>('desktop');
  const [showCode, setShowCode] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [isProcessing, setIsProcessing] = useState(false);
  const [logs, setLogs] = useState<string[]>([]);
  const iframeRef = useRef<HTMLIFrameElement>(null);

  useEffect(() => {
    const timer = setTimeout(() => {
      processComponent();
    }, 1000);

    return () => clearTimeout(timer);
  }, [code]);

  const addLog = (message: string) => {
    setLogs(prev => [...prev, `${new Date().toLocaleTimeString()}: ${message}`]);
  };

  const processComponent = async () => {
    setIsProcessing(true);
    setError(null);
    setLogs([]);
    addLog('Iniciando processamento...');

    try {
      addLog('Transformando TSX com Babel...');
      
      const result = Babel.transform(code, {
        presets: [
          ['react', { runtime: 'classic' }],
          'typescript'
        ],
        filename: 'component.tsx',
      });

      const transformedCode = result.code || '';
      addLog('✅ Babel transform concluído');
      addLog(`Código gerado: ${transformedCode.substring(0, 100)}...`);

      const htmlContent = `<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.tailwindcss.com"></script>
  <script crossorigin src="https://unpkg.com/react@18/umd/react.development.js"></script>
  <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
  <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.js"></script>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { 
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      overflow-x: hidden;
    }
  </style>
</head>
<body>
  <div id="root"></div>
  <script>
    window.onerror = function(msg, url, line, col, error) {
      console.error('ERRO:', msg, 'Linha:', line);
      document.getElementById('root').innerHTML = 
        '<div style="padding: 2rem; background: #fee; color: #c00;">' +
        '<h2>Erro JavaScript:</h2>' +
        '<p>' + msg + '</p>' +
        '<p>Linha: ' + line + '</p>' +
        '</div>';
      return true;
    };

    try {
      console.log('=== INICIANDO RENDERIZAÇÃO ===');
      
      const React = window.React;
      const ReactDOM = window.ReactDOM;
      const { useState, useEffect, useMemo, useCallback, useRef } = React;
      
      // Importar todos os ícones do Lucide
      const LucideIcons = window.lucide;
      const { 
        PlayCircle, PlusCircle, User, Target, Percent, Award, 
        BarChart3, AlertTriangle, Trophy, Lock, ChevronRight 
      } = LucideIcons;
      
      console.log('React e ícones carregados');
      
      // === MOCKS ===
      
      const useLocation = () => {
        const [location, setLocation] = useState('/');
        return [location, setLocation];
      };
      
      const useAuth = () => ({
        user: { id: '1', name: 'Diego Santos', email: 'diego@example.com' },
        loading: false,
        isAuthenticated: true,
        logout: () => console.log('logout'),
        refresh: () => console.log('refresh')
      });
      
      const trpc = {
        jogo: {
          verificarPerfil: {
            useQuery: () => ({
              data: {
                jogador: {
                  nome: 'Diego Santos',
                  ideologia: 'liberal',
                  respostasQuestionario: [1, 2, 3, 4, 5]
                }
              }
            })
          },
          getEstatisticas: {
            useQuery: () => ({
              data: { total: 12, taxaVitoria: 67, melhorResultado: 45230 }
            })
          },
          getPartidaAtiva: {
            useQuery: () => ({
              data: {
                id: '1',
                faseAtual: 2,
                decisoesTomadas: 15,
                intencaoVotos: 12450,
                finalizado: false
              }
            })
          },
          getConquistas: {
            useQuery: () => ({ data: [] })
          }
        },
        admin: {
          verificarAdmin: {
            useQuery: () => ({ data: { isAdmin: false } })
          }
        }
      };
      
      const CONQUISTAS = Array.from({ length: 25 }, (_, i) => ({
        id: 'conquista-' + (i + 1),
        nome: 'Conquista ' + (i + 1),
        icone: '🏆',
        descricao: 'Descrição'
      }));
      
      // Componentes shadcn/ui
      const Card = ({ children, className = '', onClick }) => 
        React.createElement('div', { 
          className: 'rounded-lg border bg-card text-card-foreground shadow-sm ' + className, 
          onClick 
        }, children);
      
      const CardHeader = ({ children, className = '' }) => 
        React.createElement('div', { 
          className: 'flex flex-col space-y-1.5 p-6 ' + className 
        }, children);
      
      const CardTitle = ({ children, className = '' }) => 
        React.createElement('h3', { 
          className: 'text-2xl font-semibold leading-none tracking-tight ' + className 
        }, children);
      
      const CardDescription = ({ children, className = '' }) => 
        React.createElement('p', { 
          className: 'text-sm text-muted-foreground ' + className 
        }, children);
      
      const CardContent = ({ children, className = '' }) => 
        React.createElement('div', { 
          className: 'p-6 pt-0 ' + className 
        }, children);
      
      const Button = ({ children, className = '', onClick, ...props }) => 
        React.createElement('button', { 
          className: 'inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2 ' + className, 
          onClick, 
          ...props 
        }, children);
      
      const Tooltip = ({ children }) => children;
      const TooltipProvider = ({ children }) => children;
      const TooltipTrigger = ({ asChild, children }) => children;
      const TooltipContent = ({ children, className }) => 
        React.createElement('div', { 
          className: 'rounded-md bg-popover px-3 py-1.5 text-sm text-popover-foreground shadow-md ' + className 
        }, children);
      
      const AlertDialog = ({ children, open }) => 
        open ? React.createElement('div', { 
          className: 'fixed inset-0 z-50 bg-background/80 backdrop-blur-sm' 
        }, children) : null;
      
      const AlertDialogContent = ({ children, className }) => 
        React.createElement('div', { 
          className: 'fixed left-[50%] top-[50%] z-50 grid w-full max-w-lg translate-x-[-50%] translate-y-[-50%] gap-4 border bg-background p-6 shadow-lg sm:rounded-lg ' + className 
        }, children);
      
      const AlertDialogHeader = ({ children }) => 
        React.createElement('div', { 
          className: 'flex flex-col space-y-2 text-center sm:text-left' 
        }, children);
      
      const AlertDialogTitle = ({ children, className }) => 
        React.createElement('h2', { 
          className: 'text-lg font-semibold ' + className 
        }, children);
      
      const AlertDialogDescription = ({ children, className }) => 
        React.createElement('p', { 
          className: 'text-sm text-muted-foreground ' + className 
        }, children);
      
      const AlertDialogFooter = ({ children }) => 
        React.createElement('div', { 
          className: 'flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2' 
        }, children);
      
      const AlertDialogAction = ({ children, onClick, className }) => 
        React.createElement('button', { 
          onClick, 
          className: 'inline-flex h-10 items-center justify-center rounded-md bg-primary px-4 py-2 text-sm font-semibold text-primary-foreground transition-colors hover:bg-primary/90 ' + className 
        }, children);
      
      const AlertDialogCancel = ({ children, className }) => 
        React.createElement('button', { 
          className: 'mt-2 inline-flex h-10 items-center justify-center rounded-md border px-4 py-2 text-sm font-semibold transition-colors hover:bg-accent sm:mt-0 ' + className 
        }, children);
      
      const FraseDoDia = () => 
        React.createElement('div', { className: 'bg-white/10 backdrop-blur rounded-lg p-4' },
          React.createElement('p', { className: 'text-white/90 italic' }, '"A melhor decisão beneficia a maioria."'),
          React.createElement('p', { className: 'text-green-300 text-sm mt-2' }, '- Marcelo Vitorino')
        );
      
      console.log('Mocks criados');
      
      // Código do componente
      ${transformedCode}
      
      console.log('Código executado');
      
      // Encontrar o componente
      let ComponentToRender = null;
      
      if (typeof exports !== 'undefined' && exports.default) {
        ComponentToRender = exports.default;
        console.log('Componente encontrado em exports.default');
      } else if (typeof Dashboard !== 'undefined') {
        ComponentToRender = Dashboard;
        console.log('Componente encontrado: Dashboard');
      } else if (typeof ExemploComponente !== 'undefined') {
        ComponentToRender = ExemploComponente;
        console.log('Componente encontrado: ExemploComponente');
      }
      
      if (!ComponentToRender) {
        throw new Error('Nenhum componente encontrado. Use "export default function NomeDoComponente()"');
      }
      
      console.log('Renderizando componente...');
      const root = ReactDOM.createRoot(document.getElementById('root'));
      root.render(React.createElement(ComponentToRender));
      console.log('✅ Renderização concluída!');
      
    } catch (err) {
      console.error('ERRO FATAL:', err);
      document.getElementById('root').innerHTML = 
        '<div style="padding: 2rem; background: #fee; color: #c00; font-family: monospace;">' +
        '<h2 style="margin-bottom: 1rem;">❌ Erro ao Renderizar</h2>' +
        '<p style="margin-bottom: 0.5rem;"><strong>Mensagem:</strong> ' + err.message + '</p>' +
        '<pre style="background: #f5f5f5; padding: 1rem; overflow: auto;">' + err.stack + '</pre>' +
        '</div>';
    }
  </script>
</body>
</html>`;

      if (iframeRef.current) {
        addLog('Atualizando iframe...');
        iframeRef.current.srcdoc = htmlContent;
        addLog('✅ Iframe atualizado!');
      }

      setIsProcessing(false);
    } catch (err) {
      console.error('Erro no processamento:', err);
      const errorMsg = err instanceof Error ? err.message : 'Erro desconhecido';
      setError(errorMsg);
      addLog('❌ ERRO: ' + errorMsg);
      setIsProcessing(false);
    }
  };

  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (event) => {
        const content = event.target?.result as string;
        setCode(content);
        addLog('Arquivo carregado: ' + file.name);
      };
      reader.readAsText(file);
    }
  };

  return (
    <div className="h-screen flex flex-col bg-gray-900">
      {/* Header */}
      <div className="bg-gray-800 border-b border-gray-700 p-4">
        <div className="flex items-center justify-between flex-wrap gap-3">
          <div className="flex items-center gap-3">
            <Eye className="w-6 h-6 text-blue-400" />
            <h1 className="text-xl font-bold text-white">TSX Viewer Pro</h1>
            {isProcessing ? (
              <Loader2 className="w-4 h-4 text-blue-400 animate-spin" />
            ) : (
              <CheckCircle className="w-4 h-4 text-green-400" />
            )}
          </div>
          
          <div className="flex items-center gap-2 flex-wrap">
            <button
              onClick={() => setShowCode(!showCode)}
              className="px-3 py-2 bg-gray-700 text-white rounded-lg hover:bg-gray-600 flex items-center gap-2 text-sm"
            >
              <Code className="w-4 h-4" />
              <span className="hidden sm:inline">{showCode ? 'Esconder' : 'Mostrar'}</span>
            </button>

            <label className="px-3 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700 cursor-pointer flex items-center gap-2 text-sm">
              <Upload className="w-4 h-4" />
              <span className="hidden sm:inline">Upload</span>
              <input
                type="file"
                accept=".tsx,.ts,.jsx,.js"
                onChange={handleFileUpload}
                className="hidden"
              />
            </label>

            <div className="flex gap-1 bg-gray-700 rounded-lg p-1">
              <button
                onClick={() => setViewMode('desktop')}
                className={`px-2 py-2 rounded ${viewMode === 'desktop' ? 'bg-blue-600 text-white' : 'text-gray-300 hover:text-white'}`}
              >
                <Monitor className="w-4 h-4" />
              </button>
              <button
                onClick={() => setViewMode('mobile')}
                className={`px-2 py-2 rounded ${viewMode === 'mobile' ? 'bg-blue-600 text-white' : 'text-gray-300 hover:text-white'}`}
              >
                <Smartphone className="w-4 h-4" />
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Error/Logs */}
      {(error || logs.length > 0) && (
        <div className="bg-gray-800 border-b border-gray-700 p-2 max-h-32 overflow-y-auto">
          {error && (
            <div className="bg-red-500/20 text-red-200 px-3 py-1 text-xs rounded mb-1 flex items-center gap-2">
              <AlertCircle className="w-3 h-3" />
              {error}
            </div>
          )}
          {logs.map((log, i) => (
            <div key={i} className="text-gray-400 text-xs font-mono px-3 py-0.5">
              {log}
            </div>
          ))}
        </div>
      )}

      {/* Main Content */}
      <div className="flex-1 flex overflow-hidden flex-col md:flex-row">
        {/* Code Editor */}
        {showCode && (
          <div className="w-full md:w-1/2 border-b md:border-b-0 md:border-r border-gray-700 flex flex-col h-1/2 md:h-full">
            <div className="bg-gray-800 px-4 py-2 border-b border-gray-700">
              <h2 className="text-sm font-semibold text-gray-300">Editor</h2>
            </div>
            <textarea
              value={code}
              onChange={(e) => setCode(e.target.value)}
              className="flex-1 bg-gray-900 text-gray-100 p-4 font-mono text-xs md:text-sm resize-none focus:outline-none"
              placeholder="Cole seu código TSX completo..."
              spellCheck={false}
            />
          </div>
        )}

        {/* Preview */}
        <div className={`${showCode ? 'w-full md:w-1/2 h-1/2 md:h-full' : 'w-full h-full'} flex flex-col bg-gray-100`}>
          <div className="bg-gray-800 px-4 py-2 border-b border-gray-700">
            <h2 className="text-sm font-semibold text-gray-300">
              Preview {viewMode === 'mobile' ? '📱' : '🖥️'}
            </h2>
          </div>
          <div className="flex-1 overflow-auto bg-gray-200 flex items-center justify-center p-2 md:p-4">
            <div 
              className={`bg-white ${viewMode === 'mobile' ? 'w-[375px] max-h-[667px]' : 'w-full h-full'} overflow-auto shadow-2xl`}
            >
              <iframe
                ref={iframeRef}
                className="w-full h-full border-0"
                title="Preview"
                sandbox="allow-scripts allow-same-origin"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
