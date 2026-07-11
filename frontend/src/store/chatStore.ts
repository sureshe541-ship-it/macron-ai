import { create } from 'zustand'

interface Message {
  id: string
  role: 'user' | 'assistant'
  content: string
  timestamp: string
}

interface Conversation {
  id: string
  messages: Message[]
  createdAt: string
}

interface ChatState {
  conversations: Conversation[]
  currentConversationId: string | null
  
  // Actions
  addConversation: (conversation: Conversation) => void
  addMessage: (conversationId: string, message: Message) => void
  setCurrentConversation: (id: string) => void
  clearConversation: (id: string) => void
  getAllConversations: () => Conversation[]
}

export const useChatStore = create<ChatState>((set, get) => ({
  conversations: [],
  currentConversationId: null,

  addConversation: (conversation: Conversation) => {
    set(state => ({
      conversations: [...state.conversations, conversation],
      currentConversationId: conversation.id
    }))
  },

  addMessage: (conversationId: string, message: Message) => {
    set(state => ({
      conversations: state.conversations.map(conv =>
        conv.id === conversationId
          ? { ...conv, messages: [...conv.messages, message] }
          : conv
      )
    }))
  },

  setCurrentConversation: (id: string) => {
    set({ currentConversationId: id })
  },

  clearConversation: (id: string) => {
    set(state => ({
      conversations: state.conversations.filter(conv => conv.id !== id)
    }))
  },

  getAllConversations: () => get().conversations
}))
