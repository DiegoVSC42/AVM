import React, { useState, useEffect, useRef } from 'react';
import { Copy, Check, ArrowDown, ArrowUp } from 'lucide-react';
import ReactMarkdown from 'react-markdown';
import { MODEL_COLORS, MODEL_NAMES } from '../constants';
import { chatStyles } from '../styles';

export default function ChatWindow({ model, messages, isLoading, isTyping }) {
    const messagesEndRef = useRef(null);
    const messagesTopRef = useRef(null);
    const chatContainerRef = useRef(null);
    const [copiedChat, setCopiedChat] = useState(false);
    const [copiedMessageId, setCopiedMessageId] = useState(null);
    const [shouldAutoScroll, setShouldAutoScroll] = useState(true);
    const [showScrollButtons, setShowScrollButtons] = useState(false);
    const previousMessagesRef = useRef(messages);

    const checkIfShouldAutoScroll = () => {
        if (!chatContainerRef.current) return;

        const { scrollTop, scrollHeight, clientHeight } = chatContainerRef.current;
        const distanceFromBottom = scrollHeight - scrollTop - clientHeight;

        const shouldScroll = distanceFromBottom < 100;
        setShouldAutoScroll(shouldScroll);

        setShowScrollButtons(scrollTop > 100 && distanceFromBottom > 100);
    };

    const scrollToBottom = (force = false) => {
        if ((shouldAutoScroll || force) && messagesEndRef.current) {
            messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
        }
    };

    const scrollToTop = () => {
        if (messagesTopRef.current) {
            messagesTopRef.current.scrollIntoView({ behavior: 'smooth' });
        }
    };

    useEffect(() => {
        if (isTyping) {
            setShouldAutoScroll(true);
            scrollToBottom(true);
        }
    }, [isTyping]);

    useEffect(() => {
        if (messages !== previousMessagesRef.current) {
            scrollToBottom();
            previousMessagesRef.current = messages;
        }
    }, [messages]);

    useEffect(() => {
        if (isLoading) {
            scrollToBottom();
        }
    }, [isLoading]);

    const handleScroll = () => {
        checkIfShouldAutoScroll();
    };

    const copyChat = () => {
        let chatText = `=== Chat com ${MODEL_NAMES[model]} ===\n\n`;

        messages.forEach((msg) => {
            if (msg.type === 'user') {
                chatText += `👤 Você:\n${msg.text}\n\n`;
            } else if (msg.type === 'ai') {
                chatText += `🤖 ${MODEL_NAMES[model]}:\n${msg.text}\n\n`;
            } else if (msg.type === 'error') {
                chatText += `⚠️ Erro:\n${msg.text}\n\n`;
            }
        });

        navigator.clipboard.writeText(chatText).then(() => {
            setCopiedChat(true);
            setTimeout(() => setCopiedChat(false), 2000);
        });
    };

    const copyMessage = (text, messageId) => {
        navigator.clipboard.writeText(text).then(() => {
            setCopiedMessageId(messageId);
            setTimeout(() => setCopiedMessageId(null), 2000);
        });
    };

    return (
        <div style={chatStyles.chatWindow}>
            <div style={{ ...chatStyles.chatHeader, backgroundColor: MODEL_COLORS[model] }}>
                <span>{MODEL_NAMES[model]}</span>
                <button
                    onClick={copyChat}
                    style={chatStyles.copyButton}
                    title="Copiar chat completo"
                >
                    {copiedChat ? <Check size={16} /> : <Copy size={16} />}
                </button>
            </div>

            <div
                ref={chatContainerRef}
                style={chatStyles.chatMessages}
                onScroll={handleScroll}
            >
                <div ref={messagesTopRef} />
                {messages.map((msg, idx) => (
                    <div key={idx} style={{ ...chatStyles.messageRow, justifyContent: msg.type === 'user' ? 'flex-end' : 'flex-start' }}>
                        <div style={{
                            ...chatStyles.messageBubble,
                            backgroundColor: msg.type === 'user' ? '#2563eb' : msg.type === 'error' ? '#dc2626' : '#374151'
                        }}>
                            {msg.type === 'ai' ? (
                                <>
                                    <ReactMarkdown
                                        components={{
                                            p: ({ node, ...props }) => <p style={{ margin: '0 0 8px 0', wordWrap: 'break-word', overflowWrap: 'break-word' }} {...props} />,
                                            strong: ({ node, ...props }) => <strong style={{ fontWeight: 'bold' }} {...props} />,
                                            em: ({ node, ...props }) => <em style={{ fontStyle: 'italic' }} {...props} />,
                                            ul: ({ node, ...props }) => <ul style={{ marginLeft: '20px', marginBottom: '8px' }} {...props} />,
                                            ol: ({ node, ...props }) => <ol style={{ marginLeft: '20px', marginBottom: '8px' }} {...props} />,
                                            li: ({ node, ...props }) => <li style={{ marginBottom: '4px', wordWrap: 'break-word', overflowWrap: 'break-word' }} {...props} />,
                                            h1: ({ node, ...props }) => <h1 style={{ fontSize: '18px', fontWeight: 'bold', marginBottom: '8px', wordWrap: 'break-word', overflowWrap: 'break-word' }} {...props} />,
                                            h2: ({ node, ...props }) => <h2 style={{ fontSize: '16px', fontWeight: 'bold', marginBottom: '8px', wordWrap: 'break-word', overflowWrap: 'break-word' }} {...props} />,
                                            h3: ({ node, ...props }) => <h3 style={{ fontSize: '14px', fontWeight: 'bold', marginBottom: '6px', wordWrap: 'break-word', overflowWrap: 'break-word' }} {...props} />,
                                            code: ({ node, inline, ...props }) =>
                                                inline
                                                    ? <code style={{ backgroundColor: '#1f2937', padding: '2px 4px', borderRadius: '3px', wordWrap: 'break-word', overflowWrap: 'break-word' }} {...props} />
                                                    : <code style={{ display: 'block', backgroundColor: '#1f2937', padding: '8px', borderRadius: '4px', marginBottom: '8px', overflowX: 'auto', whiteSpace: 'pre-wrap', wordWrap: 'break-word', overflowWrap: 'break-word' }} {...props} />
                                        }}
                                        style={chatStyles.messageText}
                                    >
                                        {msg.text}
                                    </ReactMarkdown>
                                    <button
                                        onClick={() => copyMessage(msg.text, `${model}-${idx}`)}
                                        style={chatStyles.copyMessageButton}
                                        title="Copiar mensagem"
                                    >
                                        {copiedMessageId === `${model}-${idx}` ? <Check size={12} /> : <Copy size={12} />}
                                    </button>
                                </>
                            ) : (
                                <div style={chatStyles.messageText}>
                                    {msg.text}
                                </div>
                            )}
                        </div>
                    </div>
                ))}

                {isLoading && (
                    <div style={{ ...chatStyles.messageRow, justifyContent: 'flex-start' }}>
                        <div style={{ ...chatStyles.messageBubble, backgroundColor: '#374151' }}>
                            <div style={chatStyles.typingIndicator}>
                                <span style={chatStyles.dot}></span>
                                <span style={{ ...chatStyles.dot, animationDelay: '0.2s' }}></span>
                                <span style={{ ...chatStyles.dot, animationDelay: '0.4s' }}></span>
                            </div>
                        </div>
                    </div>
                )}
                <div ref={messagesEndRef} />
            </div>

            {showScrollButtons && (
                <>
                    <button
                        onClick={scrollToTop}
                        style={chatStyles.scrollTopButton}
                        title="Ir para o topo"
                    >
                        <ArrowUp size={20} />
                    </button>
                    <button
                        onClick={() => scrollToBottom(true)}
                        style={chatStyles.scrollBottomButton}
                        title="Ir para o final"
                    >
                        <ArrowDown size={20} />
                    </button>
                </>
            )}
        </div>
    );
}