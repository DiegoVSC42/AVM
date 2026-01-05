import { useState, useEffect } from 'react';

export const useDevTools = () => {
  const [isEditorOpen, setIsEditorOpen] = useState(false);

  useEffect(() => {
    const handleKeyPress = (e: KeyboardEvent) => {
      // Ctrl + Shift + E para abrir/fechar o editor
      if (e.ctrlKey && e.shiftKey && e.key === 'E') {
        e.preventDefault();
        setIsEditorOpen(prev => !prev);
      }

      // Escape para fechar
      if (e.key === 'Escape' && isEditorOpen) {
        setIsEditorOpen(false);
      }
    };

    window.addEventListener('keydown', handleKeyPress);

    return () => {
      window.removeEventListener('keydown', handleKeyPress);
    };
  }, [isEditorOpen]);

  return {
    isEditorOpen,
    openEditor: () => setIsEditorOpen(true),
    closeEditor: () => setIsEditorOpen(false),
    toggleEditor: () => setIsEditorOpen(prev => !prev),
  };
};
