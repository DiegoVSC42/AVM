export const styles = {
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
        color: 'white',
        marginBottom: '8px'
    },
    modelSelector: {
        display: 'flex',
        gap: '20px'
    },
    checkboxLabel: {
        display: 'flex',
        alignItems: 'center',
        gap: '6px',
        cursor: 'pointer',
        fontSize: '14px',
        fontWeight: '500'
    },
    checkbox: {
        width: '16px',
        height: '16px',
        cursor: 'pointer'
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
        gap: '16px',
        padding: '16px',
        overflow: 'hidden'
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

export const chatStyles = {
    chatWindow: {
        display: 'flex',
        flexDirection: 'column',
        height: '100%',
        border: '1px solid #374151',
        borderRadius: '8px',
        overflow: 'hidden',
        backgroundColor: '#111827',
        position: 'relative'
    },
    chatHeader: {
        color: 'white',
        padding: '12px 16px',
        fontWeight: '600',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between'
    },
    copyButton: {
        background: 'rgba(255, 255, 255, 0.1)',
        border: 'none',
        color: 'white',
        padding: '6px',
        borderRadius: '4px',
        cursor: 'pointer',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        transition: 'background 0.2s'
    },
    chatMessages: {
        flex: 1,
        overflowY: 'auto',
        overflowX: 'hidden',
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
        color: 'white',
        position: 'relative',
        wordWrap: 'break-word',
        overflowWrap: 'break-word',
        wordBreak: 'break-word'
    },
    messageText: {
        fontSize: '14px',
        lineHeight: '1.5',
        color: 'white',
        wordWrap: 'break-word',
        overflowWrap: 'break-word',
        wordBreak: 'break-word'
    },
    copyMessageButton: {
        position: 'absolute',
        top: '8px',
        right: '8px',
        background: 'rgba(0, 0, 0, 0.3)',
        border: 'none',
        color: 'white',
        padding: '4px',
        borderRadius: '3px',
        cursor: 'pointer',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        opacity: 0.7,
        transition: 'opacity 0.2s'
    },
    scrollTopButton: {
        position: 'absolute',
        top: '70px',
        right: '16px',
        backgroundColor: '#374151',
        border: 'none',
        color: 'white',
        padding: '8px',
        borderRadius: '50%',
        cursor: 'pointer',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        boxShadow: '0 2px 8px rgba(0,0,0,0.3)',
        zIndex: 10,
        transition: 'background 0.2s'
    },
    scrollBottomButton: {
        position: 'absolute',
        bottom: '16px',
        right: '16px',
        backgroundColor: '#374151',
        border: 'none',
        color: 'white',
        padding: '8px',
        borderRadius: '50%',
        cursor: 'pointer',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        boxShadow: '0 2px 8px rgba(0,0,0,0.3)',
        zIndex: 10,
        transition: 'background 0.2s'
    },
    typingIndicator: {
        display: 'flex',
        alignItems: 'center',
        gap: '4px',
        padding: '4px 0'
    },
    dot: {
        width: '8px',
        height: '8px',
        borderRadius: '50%',
        backgroundColor: '#9ca3af',
        animation: 'bounce 1.4s infinite ease-in-out',
        display: 'inline-block'
    }
};