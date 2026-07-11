import { create } from 'zustand'

interface ChatState {
  conversationId: string | null
  messages: Array<{ id: string; role: string; content: string; timestamp: string }>
  setConversationId: (id: string | null) => void
  addMessage: (message: any) => void
  clearMessages: () => void
}

export const useChatStore = create<ChatState>((set) => ({
  conversationId: null,
  messages: [],
  setConversationId: (id) => set({ conversationId: id }),
  addMessage: (message) =>
    set((state) => ({
      messages: [...state.messages, message],
    })),
  clearMessages: () => set({ messages: [], conversationId: null }),
}))
