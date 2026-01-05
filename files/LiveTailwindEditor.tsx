import React, { useState, useEffect, useRef } from 'react';
import { Card } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { 
  Eye, EyeOff, Code, Copy, Save, RotateCcw, MousePointer2, 
  Maximize2, Minimize2, Download, AlertCircle 
} from 'lucide-react';

interface LiveTailwindEditorProps {
  isOpen: boolean;
  onClose: () => void;
}

export const LiveTailwindEditor: React.FC<LiveTailwindEditorProps> = ({ isOpen, onClose }) => {
  const [inspectMode, setInspectMode] = useState(false);
  const [selectedElement, setSelectedElement] = useState<HTMLElement | null>(null);
  const [currentClasses, setCurrentClasses] = useState<string>('');
  const [editedClasses, setEditedClasses] = useState<string>('');
  const [elementPath, setElementPath] = useState<string>('');
  const [history, setHistory] = useState<Array<{ element: HTMLElement; classes: string }>>([]);
  const [isMinimized, setIsMinimized] = useState(false);
  const overlayRef = useRef<HTMLDivElement | null>(null);

  // Visual controls state
  const [spacing, setSpacing] = useState({ p: 0, m: 0, gap: 0 });
  const [sizing, setSizing] = useState({ w: '', h: '' });
  const [colors, setColors] = useState({ bg: '', text: '', border: '' });

  useEffect(() => {
    if (inspectMode) {
      document.body.style.cursor = 'crosshair';
      document.addEventListener('click', handleElementClick, true);
      document.addEventListener('mouseover', handleElementHover);
      document.addEventListener('mouseout', handleElementOut);
    } else {
      document.body.style.cursor = 'default';
      document.removeEventListener('click', handleElementClick, true);
      document.removeEventListener('mouseover', handleElementHover);
      document.removeEventListener('mouseout', handleElementOut);
      removeOverlay();
    }

    return () => {
      document.body.style.cursor = 'default';
      document.removeEventListener('click', handleElementClick, true);
      document.removeEventListener('mouseover', handleElementHover);
      document.removeEventListener('mouseout', handleElementOut);
    };
  }, [inspectMode]);

  useEffect(() => {
    if (selectedElement) {
      const classes = selectedElement.className;
      setCurrentClasses(classes);
      setEditedClasses(classes);
      extractVisualProperties(classes);
      setElementPath(getElementPath(selectedElement));
    }
  }, [selectedElement]);

  const handleElementClick = (e: MouseEvent) => {
    e.preventDefault();
    e.stopPropagation();
    
    const target = e.target as HTMLElement;
    
    // Ignore clicks on the editor itself
    if (target.closest('#live-tailwind-editor')) {
      return;
    }

    setSelectedElement(target);
    setInspectMode(false);
  };

  const handleElementHover = (e: MouseEvent) => {
    const target = e.target as HTMLElement;
    
    if (target.closest('#live-tailwind-editor')) {
      return;
    }

    showOverlay(target);
  };

  const handleElementOut = () => {
    removeOverlay();
  };

  const showOverlay = (element: HTMLElement) => {
    removeOverlay();
    
    const rect = element.getBoundingClientRect();
    const overlay = document.createElement('div');
    overlay.id = 'element-hover-overlay';
    overlay.style.cssText = `
      position: fixed;
      top: ${rect.top}px;
      left: ${rect.left}px;
      width: ${rect.width}px;
      height: ${rect.height}px;
      border: 2px solid #3b82f6;
      background: rgba(59, 130, 246, 0.1);
      pointer-events: none;
      z-index: 9998;
      box-sizing: border-box;
    `;
    
    document.body.appendChild(overlay);
    overlayRef.current = overlay;
  };

  const removeOverlay = () => {
    const existing = document.getElementById('element-hover-overlay');
    if (existing) {
      existing.remove();
    }
  };

  const getElementPath = (element: HTMLElement): string => {
    const path: string[] = [];
    let current: HTMLElement | null = element;
    
    while (current && current !== document.body) {
      let selector = current.tagName.toLowerCase();
      
      if (current.id) {
        selector += `#${current.id}`;
      } else if (current.className) {
        const classes = current.className.split(' ').slice(0, 2).join('.');
        if (classes) selector += `.${classes}`;
      }
      
      path.unshift(selector);
      current = current.parentElement;
    }
    
    return path.join(' > ');
  };

  const extractVisualProperties = (classes: string) => {
    const classArray = classes.split(' ');
    
    // Extract padding
    const pClass = classArray.find(c => c.startsWith('p-'));
    setSpacing(prev => ({ ...prev, p: pClass ? parseInt(pClass.split('-')[1]) : 0 }));
    
    // Extract margin
    const mClass = classArray.find(c => c.startsWith('m-'));
    setSpacing(prev => ({ ...prev, m: mClass ? parseInt(mClass.split('-')[1]) : 0 }));
    
    // Extract gap
    const gapClass = classArray.find(c => c.startsWith('gap-'));
    setSpacing(prev => ({ ...prev, gap: gapClass ? parseInt(gapClass.split('-')[1]) : 0 }));
    
    // Extract width
    const wClass = classArray.find(c => c.startsWith('w-'));
    setSizing(prev => ({ ...prev, w: wClass || '' }));
    
    // Extract height
    const hClass = classArray.find(c => c.startsWith('h-'));
    setSizing(prev => ({ ...prev, h: hClass || '' }));
    
    // Extract colors
    const bgClass = classArray.find(c => c.startsWith('bg-'));
    const textClass = classArray.find(c => c.startsWith('text-') && !c.includes('text-['));
    const borderClass = classArray.find(c => c.startsWith('border-') && !c.includes('border-['));
    
    setColors({
      bg: bgClass || '',
      text: textClass || '',
      border: borderClass || ''
    });
  };

  const applyClasses = () => {
    if (!selectedElement) return;
    
    // Save to history
    setHistory(prev => [...prev, { element: selectedElement, classes: currentClasses }]);
    
    selectedElement.className = editedClasses;
    setCurrentClasses(editedClasses);
    
    alert('Classes aplicadas! Use Ctrl+Z para desfazer.');
  };

  const undoLastChange = () => {
    if (history.length === 0) return;
    
    const last = history[history.length - 1];
    last.element.className = last.classes;
    
    setHistory(prev => prev.slice(0, -1));
    
    if (selectedElement === last.element) {
      setCurrentClasses(last.classes);
      setEditedClasses(last.classes);
    }
  };

  const copyToClipboard = () => {
    if (!selectedElement) return;
    
    const code = `<${selectedElement.tagName.toLowerCase()} className="${editedClasses}">
  {/* Conteúdo */}
</${selectedElement.tagName.toLowerCase()}>`;
    
    navigator.clipboard.writeText(code);
    alert('Código copiado para área de transferência!');
  };

  const updateClassWithVisual = (type: 'spacing' | 'sizing' | 'colors', key: string, value: string | number) => {
    const classArray = editedClasses.split(' ').filter(Boolean);
    
    let prefix = '';
    let newClass = '';
    
    if (type === 'spacing') {
      prefix = key;
      newClass = `${prefix}-${value}`;
    } else if (type === 'sizing') {
      newClass = value as string;
    } else if (type === 'colors') {
      newClass = value as string;
    }
    
    // Remove old class with same prefix
    const filtered = classArray.filter(c => {
      if (type === 'spacing') return !c.startsWith(`${prefix}-`);
      if (type === 'sizing') return !c.startsWith(key);
      if (type === 'colors') {
        if (key === 'bg') return !c.startsWith('bg-');
        if (key === 'text') return !c.startsWith('text-') || c.includes('text-[');
        if (key === 'border') return !c.startsWith('border-') || c.includes('border-[');
      }
      return true;
    });
    
    // Add new class
    if (newClass) {
      filtered.push(newClass);
    }
    
    setEditedClasses(filtered.join(' '));
  };

  if (!isOpen) return null;

  return (
    <div
      id="live-tailwind-editor"
      className={`fixed ${isMinimized ? 'bottom-4 right-4' : 'top-4 right-4'} z-[9999] 
        ${isMinimized ? 'w-auto' : 'w-96'} max-h-[90vh] overflow-auto`}
    >
      <Card className="bg-white shadow-2xl border-2 border-blue-500">
        {/* Header */}
        <div className="flex items-center justify-between p-4 border-b bg-blue-50">
          <div className="flex items-center gap-2">
            <Code className="w-5 h-5 text-blue-600" />
            <h3 className="font-bold text-blue-900">Live Tailwind Editor</h3>
          </div>
          <div className="flex gap-2">
            <Button
              size="sm"
              variant="ghost"
              onClick={() => setIsMinimized(!isMinimized)}
            >
              {isMinimized ? <Maximize2 className="w-4 h-4" /> : <Minimize2 className="w-4 h-4" />}
            </Button>
            <Button size="sm" variant="ghost" onClick={onClose}>
              <EyeOff className="w-4 h-4" />
            </Button>
          </div>
        </div>

        {!isMinimized && (
          <div className="p-4 space-y-4">
            {/* Inspect Mode */}
            <div className="space-y-2">
              <Button
                onClick={() => setInspectMode(!inspectMode)}
                variant={inspectMode ? 'default' : 'outline'}
                className="w-full"
              >
                <MousePointer2 className="w-4 h-4 mr-2" />
                {inspectMode ? 'Clique no elemento' : 'Inspecionar Elemento'}
              </Button>
              
              {inspectMode && (
                <div className="flex items-center gap-2 text-sm text-amber-600 bg-amber-50 p-2 rounded">
                  <AlertCircle className="w-4 h-4" />
                  Clique em qualquer elemento da página
                </div>
              )}
            </div>

            {/* Selected Element Info */}
            {selectedElement && (
              <>
                <div className="p-3 bg-gray-50 rounded text-xs space-y-1">
                  <div className="font-mono text-gray-600">
                    {elementPath}
                  </div>
                  <div className="text-gray-500">
                    {selectedElement.tagName.toLowerCase()}
                  </div>
                </div>

                <Tabs defaultValue="visual" className="w-full">
                  <TabsList className="grid w-full grid-cols-2">
                    <TabsTrigger value="visual">Visual</TabsTrigger>
                    <TabsTrigger value="code">Código</TabsTrigger>
                  </TabsList>

                  {/* Visual Tab */}
                  <TabsContent value="visual" className="space-y-4">
                    {/* Spacing Controls */}
                    <div className="space-y-2">
                      <Label className="text-sm font-semibold">Espaçamento</Label>
                      
                      <div className="space-y-2">
                        <Label className="text-xs">Padding</Label>
                        <div className="flex items-center gap-2">
                          <Input
                            type="range"
                            min="0"
                            max="32"
                            step="1"
                            value={spacing.p}
                            onChange={(e) => {
                              const val = e.target.value;
                              setSpacing(prev => ({ ...prev, p: parseInt(val) }));
                              updateClassWithVisual('spacing', 'p', val);
                            }}
                            className="flex-1"
                          />
                          <span className="text-sm w-12 text-right">p-{spacing.p}</span>
                        </div>
                      </div>

                      <div className="space-y-2">
                        <Label className="text-xs">Margin</Label>
                        <div className="flex items-center gap-2">
                          <Input
                            type="range"
                            min="0"
                            max="32"
                            step="1"
                            value={spacing.m}
                            onChange={(e) => {
                              const val = e.target.value;
                              setSpacing(prev => ({ ...prev, m: parseInt(val) }));
                              updateClassWithVisual('spacing', 'm', val);
                            }}
                            className="flex-1"
                          />
                          <span className="text-sm w-12 text-right">m-{spacing.m}</span>
                        </div>
                      </div>

                      <div className="space-y-2">
                        <Label className="text-xs">Gap</Label>
                        <div className="flex items-center gap-2">
                          <Input
                            type="range"
                            min="0"
                            max="32"
                            step="1"
                            value={spacing.gap}
                            onChange={(e) => {
                              const val = e.target.value;
                              setSpacing(prev => ({ ...prev, gap: parseInt(val) }));
                              updateClassWithVisual('spacing', 'gap', val);
                            }}
                            className="flex-1"
                          />
                          <span className="text-sm w-12 text-right">gap-{spacing.gap}</span>
                        </div>
                      </div>
                    </div>

                    {/* Quick Size Buttons */}
                    <div className="space-y-2">
                      <Label className="text-sm font-semibold">Largura</Label>
                      <div className="grid grid-cols-4 gap-2">
                        {['w-full', 'w-1/2', 'w-1/3', 'w-auto'].map(w => (
                          <Button
                            key={w}
                            size="sm"
                            variant={sizing.w === w ? 'default' : 'outline'}
                            onClick={() => {
                              setSizing(prev => ({ ...prev, w }));
                              updateClassWithVisual('sizing', 'w-', w);
                            }}
                            className="text-xs"
                          >
                            {w.split('-')[1]}
                          </Button>
                        ))}
                      </div>
                    </div>

                    {/* Color Presets */}
                    <div className="space-y-2">
                      <Label className="text-sm font-semibold">Cor de Fundo</Label>
                      <div className="grid grid-cols-5 gap-2">
                        {['bg-white', 'bg-gray-100', 'bg-blue-500', 'bg-green-500', 'bg-red-500'].map(bg => (
                          <button
                            key={bg}
                            onClick={() => {
                              setColors(prev => ({ ...prev, bg }));
                              updateClassWithVisual('colors', 'bg', bg);
                            }}
                            className={`h-8 rounded border-2 ${bg} ${colors.bg === bg ? 'border-black' : 'border-gray-300'}`}
                          />
                        ))}
                      </div>
                    </div>
                  </TabsContent>

                  {/* Code Tab */}
                  <TabsContent value="code" className="space-y-4">
                    <div className="space-y-2">
                      <Label>Classes Atuais</Label>
                      <div className="p-2 bg-gray-100 rounded text-xs font-mono break-all">
                        {currentClasses}
                      </div>
                    </div>

                    <div className="space-y-2">
                      <Label>Classes Editadas</Label>
                      <textarea
                        value={editedClasses}
                        onChange={(e) => setEditedClasses(e.target.value)}
                        className="w-full h-32 p-2 border rounded text-xs font-mono"
                        placeholder="Digite as classes Tailwind..."
                      />
                    </div>
                  </TabsContent>
                </Tabs>

                {/* Action Buttons */}
                <div className="flex gap-2">
                  <Button
                    onClick={applyClasses}
                    className="flex-1"
                    size="sm"
                  >
                    <Save className="w-4 h-4 mr-2" />
                    Aplicar
                  </Button>
                  <Button
                    onClick={copyToClipboard}
                    variant="outline"
                    size="sm"
                  >
                    <Copy className="w-4 h-4" />
                  </Button>
                  <Button
                    onClick={undoLastChange}
                    variant="outline"
                    size="sm"
                    disabled={history.length === 0}
                  >
                    <RotateCcw className="w-4 h-4" />
                  </Button>
                </div>

                {/* Export Button */}
                <Button
                  onClick={() => {
                    const data = history.map(h => ({
                      path: getElementPath(h.element),
                      oldClasses: h.classes,
                      newClasses: h.element.className
                    }));
                    
                    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
                    const url = URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = 'tailwind-changes.json';
                    a.click();
                    URL.revokeObjectURL(url);
                  }}
                  variant="outline"
                  size="sm"
                  className="w-full"
                  disabled={history.length === 0}
                >
                  <Download className="w-4 h-4 mr-2" />
                  Exportar Mudanças
                </Button>
              </>
            )}
          </div>
        )}
      </Card>
    </div>
  );
};
