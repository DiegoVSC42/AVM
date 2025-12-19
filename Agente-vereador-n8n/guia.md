# Comparador de Modelos IA - Setup Local

## 1️⃣ Criar a estrutura do projeto

Abra o terminal e execute:

```bash
# Criar pasta do projeto
mkdir comparador-ia
cd comparador-ia

# Criar estrutura
mkdir src
```

## 2️⃣ Criar os arquivos

### package.json

```json
{
  "name": "comparador-ia",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "lucide-react": "^0.263.1"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.0.0",
    "vite": "^4.3.9"
  }
}
```

### vite.config.js

```js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000
  }
})
```

### index.html

```html
<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Comparador de Modelos IA</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
```

### src/main.jsx

```jsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
```

### src/index.css

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#root {
  width: 100%;
  height: 100vh;
}
```

### src/App.jsx

```jsx
import React, { useState } from 'react';
import { Send, Loader2, Download } from 'lucide-react';

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
                <div style={styles.messageText}>
                  {msg.text}
                </div>
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
    whiteSpace: 'pre-wrap',
    wordBreak: 'break-word',
    fontSize: '14px'
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

## 3️⃣ Instalar dependências e rodar

```bash
# Instalar dependências
npm install

# Rodar o projeto
npm run dev
```

## 4️⃣ Acessar

Abra o navegador em: **<http://localhost:3000>**

---

## 🔧 Se ainda der erro de CORS

Adicione esta variável de ambiente no seu n8n:

```bash
N8N_CORS_ORIGIN=http://localhost:3000
```

Ou use `*` para aceitar de qualquer origem:

```bash
N8N_CORS_ORIGIN=*
```

---

## 📦 Estrutura final dos arquivos

```
comparador-ia/
├── package.json
├── vite.config.js
├── index.html
└── src/
    ├── main.jsx
    ├── index.css
    └── App.jsx
```
