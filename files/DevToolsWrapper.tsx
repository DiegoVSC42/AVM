import React from 'react';
import { LiveTailwindEditor } from './LiveTailwindEditor';
import { useDevTools } from './useDevTools';

export const DevToolsWrapper: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const { isEditorOpen, closeEditor } = useDevTools();

  // Apenas em desenvolvimento
  const isDev = import.meta.env.DEV;

  return (
    <>
      {children}
      
      {isDev && (
        <>
          <LiveTailwindEditor isOpen={isEditorOpen} onClose={closeEditor} />
          
          {/* Floating hint */}
          {!isEditorOpen && (
            <div className="fixed bottom-4 left-4 bg-black/80 text-white text-xs px-3 py-2 rounded-full z-[9998] pointer-events-none">
              Pressione <kbd className="bg-white/20 px-1.5 py-0.5 rounded">Ctrl + Shift + E</kbd> para editar layout
            </div>
          )}
        </>
      )}
    </>
  );
};
