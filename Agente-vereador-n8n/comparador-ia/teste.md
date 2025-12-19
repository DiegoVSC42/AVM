# Comparador de Modelos IA - Setup Local

## 1️⃣ Instalar biblioteca de markdown

```bash
npm install react-markdown
```

## 2️⃣ Atualizar o src/App.jsx

```jsx
import React, { useState } from 'react';
import { Send, Loader2, Download } from 'lucide-react';
import ReactMarkdown from 'react-markdown';

const WEBHOOKS = {
  gemini: 'https://n8n.academiavitorinoemendonca.com.br/webhook/Gemini',
  gpt: 'https://n8n.academiavitorinoemendonca.com.br/webhook/GPT',
  claude: 'https://n8n.academiavitorinoemendonca.com.br/webhook/Claude'
};

export default function App() {
  const [message, setMessage] = useState('');
  const [conversations, setConversations] = useState({
    gemini: [],
    gpt: [],
    claude: []
  });
  const [loading, setLoading] = useState({
    gemini: false,
    gpt: false,
    claude: false
  });
  const [logs, setLogs] = useState([]);

  const sendMessage = async () => {
    if (!message.trim()) return;

    const userMessage = message.trim();
    setMessage('');

    const newConversations = {
      gemini: [...conversations.gemini, { type: 'user', text: userMessage }],
      gpt: [...conversations.gpt, { type: 'user', text: userMessage }],
      claude: [...conversations.claude, { type: 'user', text: userMessage }]
    };
    setConversations(newConversations);

    setLoading({ gemini: true, gpt: true, claude: true });

    const timestamp = new Date().toISOString();

    const requests = Object.entries(WEBHOOKS).map(async ([model, url]) => {
      try {
        const response = await fetch(url, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ message: userMessage })
        });

        const data = await response.text();

        setConversations(prev => ({
          ...prev,
          [model]: [...prev[model], { type: 'ai', text: data }]
        }));

        setLogs(prev => [...prev, {
          timestamp,
          model,
          message: userMessage,
          response: data,
          success: true
        }]);

        setLoading(prev => ({ ...prev, [model]: false }));
      } catch (error) {
        console.error(`Erro ${model}:`, error);
        const errorMsg = `❌ Erro: ${error.message}`;
        
        setConversations(prev => ({
          ...prev,
          [model]: [...prev[model], { type: 'error', text: errorMsg }]
        }));

        setLogs(prev => [...prev, {
          timestamp,
          model,
          message: userMessage,
          response: errorMsg,
          success: false,
          error: error.message
        }]);

        setLoading(prev => ({ ...prev, [model]: false }));
      }
    });

    await Promise.all(requests);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const exportLogs = () => {
    const logsJson = JSON.stringify(logs, null, 2);
    const blob = new Blob([logsJson], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `logs_${new Date().toISOString()}.json`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const ChatWindow = ({ model, messages, isLoading }) => {
    const modelColors = {
      gemini: 'bg-blue-600',
      gpt: 'bg-green-600',
      claude: 'bg-purple-600'
    };

    const modelNames = {
      gemini: 'Gemini',
      gpt: 'GPT',
      claude: 'Claude'
    };

    return (
      <div style={styles.chatWindow}>
        <div style={{...styles.chatHeader, backgroundColor: modelColors[model] === 'bg-blue-600' ? '#2563eb' : modelColors[model] === 'bg-green-600' ? '#16a34a' : '#9333ea'}}>
          {modelNames[model]}
        </div>
        
        <div style={styles.chatMessages}>
          {messages.map((msg, idx) => (
            <div key={idx} style={{...styles.messageRow, justifyContent: msg.type === 'user' ? 'flex-end' : 'flex-start'}}>
              <div style={{
                ...styles.messageBubble,
                backgroundColor: msg.type === 'user' ? '#2563eb' : msg.type === 'error' ? '#dc2626' : '#374151'
              }}>
                {msg.type === 'ai' ? (
                  <ReactMarkdown
                    components={{
                      p: ({node, ...props}) => <p style={{margin: '0 0 8px 0'}} {...props} />,
                      strong: ({node, ...props}) => <strong style={{fontWeight: 'bold'}} {...props} />,
                      em: ({node, ...props}) => <em style={{fontStyle: 'italic'}} {...props} />,
                      ul: ({node, ...props}) => <ul style={{marginLeft: '20px', marginBottom: '8px'}} {...props} />,
                      ol: ({node, ...props}) => <ol style={{marginLeft: '20px', marginBottom: '8px'}} {...props} />,
                      li: ({node, ...props}) => <li style={{marginBottom: '4px'}} {...props} />,
                      h1: ({node, ...props}) => <h1 style={{fontSize: '18px', fontWeight: 'bold', marginBottom: '8px'}} {...props} />,
                      h2: ({node, ...props}) => <h2 style={{fontSize: '16px', fontWeight: 'bold', marginBottom: '8px'}} {...props} />,
                      h3: ({node, ...props}) => <h3 style={{fontSize: '14px', fontWeight: 'bold', marginBottom: '6px'}} {...props} />,
                      code: ({node, inline, ...props}) => 
                        inline 
                          ? <code style={{backgroundColor: '#1f2937', padding: '2px 4px', borderRadius: '3px'}} {...props} />
                          : <code style={{display: 'block', backgroundColor: '#1f2937', padding: '8px', borderRadius: '4px', marginBottom: '8px'}} {...props} />
                    }}
                    style={styles.messageText}
                  >
                    {msg.text}
                  </ReactMarkdown>
                ) : (
                  <div style={styles.messageText}>
                    {msg.text}
                  </div>
                )}
              </div>
            </div>
          ))}
          
          {isLoading && (
            <div style={{...styles.messageRow, justifyContent: 'flex-start'}}>
              <div style={{...styles.messageBubble, backgroundColor: '#374151'}}>
                <Loader2 style={{width: 20, height: 20, animation: 'spin 1s linear infinite'}} />
              </div>
            </div>
          )}
        </div>
      </div>
    );
  };

  return (
    <div style={styles.container}>
      <div style={styles.header}>
        <div style={styles.headerContent}>
          <h1 style={styles.title}>Comparador de Modelos IA</h1>
          <button
            onClick={exportLogs}
            style={styles.exportButton}
            disabled={logs.length === 0}
          >
            <Download style={{width: 16, height: 16}} />
            Exportar Logs ({logs.length})
          </button>
        </div>
      </div>

      <div style={styles.chatGrid}>
        <ChatWindow model="gemini" messages={conversations.gemini} isLoading={loading.gemini} />
        <ChatWindow model="gpt" messages={conversations.gpt} isLoading={loading.gpt} />
        <ChatWindow model="claude" messages={conversations.claude} isLoading={loading.claude} />
      </div>

      <div style={styles.footer}>
        <div style={styles.inputContainer}>
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Digite sua mensagem para comparar as respostas..."
            style={styles.input}
            disabled={loading.gemini || loading.gpt || loading.claude}
          />
          <button
            onClick={sendMessage}
            disabled={!message.trim() || loading.gemini || loading.gpt || loading.claude}
            style={styles.sendButton}
          >
            {loading.gemini || loading.gpt || loading.claude ? (
              <Loader2 style={{width: 20, height: 20}} />
            ) : (
              <Send style={{width: 20, height: 20}} />
            )}
            Enviar
          </button>
        </div>
      </div>
    </div>
  );
}

const styles = {
  container: {
    height: '100vh',
    backgroundColor: '#030712',
    display: 'flex',
    flexDirection: 'column'
  },
  header: {
    backgroundColor: '#111827',
    borderBottom: '1px solid #374151',
    padding: '16px 24px'
  },
  headerContent: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between'
  },
  title: {
    fontSize: '24px',
    fontWeight: 'bold',
    color: 'white'
  },
  exportButton: {
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    backgroundColor: '#374151',
    color: 'white',
    padding: '8px 16px',
    borderRadius: '8px',
    border: 'none',
    cursor: 'pointer',
    fontSize: '14px'
  },
  chatGrid: {
    flex: 1,
    display: 'grid',
    gridTemplateColumns: 'repeat(3, 1fr)',
    gap: '16px',
    padding: '16px',
    overflow: 'hidden'
  },
  chatWindow: {
    display: 'flex',
    flexDirection: 'column',
    height: '100%',
    border: '1px solid #374151',
    borderRadius: '8px',
    overflow: 'hidden',
    backgroundColor: '#111827'
  },
  chatHeader: {
    color: 'white',
    padding: '12px 16px',
    fontWeight: '600',
    textAlign: 'center'
  },
  chatMessages: {
    flex: 1,
    overflowY: 'auto',
    padding: '16px',
    display: 'flex',
    flexDirection: 'column',
    gap: '16px',
    backgroundColor: '#1f2937'
  },
  messageRow: {
    display: 'flex'
  },
  messageBubble: {
    maxWidth: '80%',
    borderRadius: '8px',
    padding: '12px 16px',
    color: 'white'
  },
  messageText: {
    fontSize: '14px',
    lineHeight: '1.5',
    color: 'white'
  },
  footer: {
    backgroundColor: '#111827',
    borderTop: '1px solid #374151',
    padding: '16px 24px'
  },
  inputContainer: {
    maxWidth: '1024px',
    margin: '0 auto',
    display: 'flex',
    gap: '12px'
  },
  input: {
    flex: 1,
    backgroundColor: '#1f2937',
    color: 'white',
    border: '1px solid #374151',
    borderRadius: '8px',
    padding: '12px 16px',
    fontSize: '14px',
    outline: 'none'
  },
  sendButton: {
    backgroundColor: '#2563eb',
    color: 'white',
    padding: '12px 24px',
    borderRadius: '8px',
    border: 'none',
    cursor: 'pointer',
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    fontWeight: '600',
    fontSize: '14px'
  }
};
```

## 3️⃣ Execute os comandos

```bash
# Instalar a biblioteca de markdown
npm install react-markdown

# Reiniciar o servidor (Ctrl+C e depois)
npm run dev
```

Agora o texto vai aparecer formatado com **negrito**, *itálico*, listas, etc, sem os asteriscos! 🎉