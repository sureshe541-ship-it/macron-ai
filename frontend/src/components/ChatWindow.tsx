import { useState, useRef, useEffect } from 'react'
import { useChatStore } from '../store/chatStore'
import { apiClient } from '../utils/api'
import MessageBubble from './MessageBubble'
import '../styles/ChatWindow.css'

interface Message {
  id: string
  role: 'user' | 'assistant'
  content: string
  timestamp: string
}

export default function ChatWindow() {
  const [input, setInput] = useState('')
  const [messages, setMessages] = useState<Message[]>([])
  const [loading, setLoading] = useState(false)
  const [conversationId, setConversationId] = useState<string | null>(null)
  const messagesEndRef = useRef<HTMLDivElement>(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const handleSendMessage = async (e: React.FormEvent) => {
    e.preventDefault()
    
    if (!input.trim()) return

    setLoading(true)
    
    try {
      // Add user message to UI
      const userMessage: Message = {
        id: Date.now().toString(),
        role: 'user',
        content: input,
        timestamp: new Date().toISOString()
      }
      setMessages(prev => [...prev, userMessage])

      // Send to API
      const response = await apiClient.post('/api/chat', {
        message: input,
        conversation_id: conversationId,
        context: ''
      })

      // Add assistant response
      const assistantMessage: Message = {
        id: response.data.message_id,
        role: 'assistant',
        content: response.data.response,
        timestamp: new Date().toISOString()
      }
      setMessages(prev => [...prev, assistantMessage])
      
      if (!conversationId) {
        setConversationId(response.data.conversation_id)
      }

      setInput('')
    } catch (error) {
      console.error('Error sending message:', error)
      const errorMessage: Message = {
        id: 'error-' + Date.now(),
        role: 'assistant',
        content: 'Sorry, there was an error processing your request. Please try again.',
        timestamp: new Date().toISOString()
      }
      setMessages(prev => [...prev, errorMessage])
    } finally {
      setLoading(false)
    }
  }

  const handleClearChat = () => {
    setMessages([])
    setConversationId(null)
    setInput('')
  }

  return (
    <div className="chat-window">
      <div className="chat-header">
        <h2>AI Chat Assistant</h2>
        {messages.length > 0 && (
          <button className="clear-btn" onClick={handleClearChat}>
            Clear Chat
          </button>
        )}
      </div>

      <div className="chat-messages">
        {messages.length === 0 ? (
          <div className="empty-state">
            <p>👋 Start a conversation with AI</p>
            <p>Ask questions, get analysis, or just chat!</p>
          </div>
        ) : (
          messages.map(message => (
            <MessageBubble 
              key={message.id} 
              message={message}
            />
          ))
        )}
        {loading && (
          <div className="message-group assistant">
            <div className="typing-indicator">
              <span></span><span></span><span></span>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <form className="chat-input-form" onSubmit={handleSendMessage}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
          disabled={loading}
          className="chat-input"
        />
        <button 
          type="submit" 
          disabled={loading || !input.trim()}
          className="send-btn"
        >
          {loading ? '...' : 'Send'}
        </button>
      </form>
    </div>
  )
}
