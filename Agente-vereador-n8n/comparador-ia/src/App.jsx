import React, { useState } from 'react';
import { Send, Loader2, Download } from 'lucide-react';
import ChatWindow from './components/ChatWindow';
import { WEBHOOKS } from './constants';
import { styles } from './styles';

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
    const [activeModels, setActiveModels] = useState({
        gemini: true,
        gpt: true,
        claude: true
    });
    const [isTyping, setIsTyping] = useState(false);

    const toggleModel = (model) => {
        setActiveModels(prev => ({
            ...prev,
            [model]: !prev[model]
        }));
    };

    const getActiveModels = () => {
        return Object.entries(activeModels)
            .filter(([_, isActive]) => isActive)
            .map(([model, _]) => model);
    };

    const handleInputChange = (e) => {
        setMessage(e.target.value);
        setIsTyping(true);
        setTimeout(() => setIsTyping(false), 100);
    };

    const sendMessage = async () => {
        if (!message.trim()) return;

        const userMessage = message.trim();
        setMessage('');

        const activeModelsList = getActiveModels();
        if (activeModelsList.length === 0) {
            alert('Selecione pelo menos um modelo!');
            return;
        }

        const newConversations = { ...conversations };
        activeModelsList.forEach(model => {
            newConversations[model] = [...conversations[model], { type: 'user', text: userMessage }];
        });
        setConversations(newConversations);

        const newLoading = { ...loading };
        activeModelsList.forEach(model => {
            newLoading[model] = true;
        });
        setLoading(newLoading);

        const timestamp = new Date().toISOString();

        const logEntry = {
            timestamp,
            message: userMessage,
            responseGemini: activeModels.gemini ? null : undefined,
            responseGPT: activeModels.gpt ? null : undefined,
            responseClaude: activeModels.claude ? null : undefined
        };

        const logIndex = logs.length;
        setLogs(prev => [...prev, logEntry]);

        const requests = activeModelsList.map(async (model) => {
            const url = WEBHOOKS[model];
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

                setLogs(prev => {
                    const updatedLogs = [...prev];
                    if (model === 'gemini') {
                        updatedLogs[logIndex].responseGemini = data;
                    } else if (model === 'gpt') {
                        updatedLogs[logIndex].responseGPT = data;
                    } else if (model === 'claude') {
                        updatedLogs[logIndex].responseClaude = data;
                    }
                    return updatedLogs;
                });

                setLoading(prev => ({ ...prev, [model]: false }));
            } catch (error) {
                console.error(`Erro ${model}:`, error);
                const errorMsg = `❌ Erro: ${error.message}`;

                setConversations(prev => ({
                    ...prev,
                    [model]: [...prev[model], { type: 'error', text: errorMsg }]
                }));

                setLogs(prev => {
                    const updatedLogs = [...prev];
                    if (model === 'gemini') {
                        updatedLogs[logIndex].responseGemini = errorMsg;
                    } else if (model === 'gpt') {
                        updatedLogs[logIndex].responseGPT = errorMsg;
                    } else if (model === 'claude') {
                        updatedLogs[logIndex].responseClaude = errorMsg;
                    }
                    return updatedLogs;
                });

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

    const activeModelsList = getActiveModels();
    const gridColumns = activeModelsList.length;
    const isAnyLoading = activeModelsList.some(model => loading[model]);

    return (
        <>
            <style>
                {`
                    @keyframes bounce {
                        0%, 60%, 100% {
                            transform: translateY(0);
                            opacity: 0.7;
                        }
                        30% {
                            transform: translateY(-10px);
                            opacity: 1;
                        }
                    }
                    
                    @keyframes spin {
                        from {
                            transform: rotate(0deg);
                        }
                        to {
                            transform: rotate(360deg);
                        }
                    }
                    
                    .spinning {
                        animation: spin 1s linear infinite;
                    }
                `}
            </style>
            <div style={styles.container}>
                <div style={styles.header}>
                    <div style={styles.headerContent}>
                        <div>
                            <h1 style={styles.title}>Comparador de Modelos IA</h1>
                            <div style={styles.modelSelector}>
                                <label style={styles.checkboxLabel}>
                                    <input
                                        type="checkbox"
                                        checked={activeModels.gemini}
                                        onChange={() => toggleModel('gemini')}
                                        style={styles.checkbox}
                                    />
                                    <span style={{ color: '#60a5fa' }}>Gemini</span>
                                </label>
                                <label style={styles.checkboxLabel}>
                                    <input
                                        type="checkbox"
                                        checked={activeModels.gpt}
                                        onChange={() => toggleModel('gpt')}
                                        style={styles.checkbox}
                                    />
                                    <span style={{ color: '#4ade80' }}>GPT</span>
                                </label>
                                <label style={styles.checkboxLabel}>
                                    <input
                                        type="checkbox"
                                        checked={activeModels.claude}
                                        onChange={() => toggleModel('claude')}
                                        style={styles.checkbox}
                                    />
                                    <span style={{ color: '#c084fc' }}>Claude</span>
                                </label>
                            </div>
                        </div>
                        <button
                            onClick={exportLogs}
                            style={styles.exportButton}
                            disabled={logs.length === 0}
                        >
                            <Download style={{ width: 16, height: 16 }} />
                            Exportar Logs ({logs.length})
                        </button>
                    </div>
                </div>

                <div style={{
                    ...styles.chatGrid,
                    gridTemplateColumns: `repeat(${gridColumns}, 1fr)`
                }}>
                    {activeModels.gemini && <ChatWindow model="gemini" messages={conversations.gemini} isLoading={loading.gemini} isTyping={isTyping} />}
                    {activeModels.gpt && <ChatWindow model="gpt" messages={conversations.gpt} isLoading={loading.gpt} isTyping={isTyping} />}
                    {activeModels.claude && <ChatWindow model="claude" messages={conversations.claude} isLoading={loading.claude} isTyping={isTyping} />}
                </div>

                <div style={styles.footer}>
                    <div style={styles.inputContainer}>
                        <input
                            type="text"
                            value={message}
                            onChange={handleInputChange}
                            onKeyPress={handleKeyPress}
                            placeholder="Digite sua mensagem para comparar as respostas..."
                            style={styles.input}
                            disabled={isAnyLoading}
                        />
                        <button
                            onClick={sendMessage}
                            disabled={!message.trim() || isAnyLoading}
                            style={styles.sendButton}
                        >
                            {isAnyLoading ? (
                                <Loader2 className="spinning" style={{ width: 20, height: 20 }} />
                            ) : (
                                <Send style={{ width: 20, height: 20 }} />
                            )}
                            Enviar
                        </button>
                    </div>
                </div>
            </div>
        </>
    );
}