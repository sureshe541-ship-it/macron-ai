import { useState } from 'react'
import ChatWindow from './components/ChatWindow'
import AnalysisPanel from './components/AnalysisPanel'
import './App.css'

function App() {
  const [activeTab, setActiveTab] = useState<'chat' | 'analysis'>('chat')

  return (
    <div className="app">
      <header className="app-header">
        <h1>🤖 Macron AI</h1>
        <p>Real AI-powered application</p>
      </header>

      <nav className="tab-navigation">
        <button 
          className={`tab-btn ${activeTab === 'chat' ? 'active' : ''}`}
          onClick={() => setActiveTab('chat')}
        >
          Chat
        </button>
        <button 
          className={`tab-btn ${activeTab === 'analysis' ? 'active' : ''}`}
          onClick={() => setActiveTab('analysis')}
        >
          Analysis
        </button>
      </nav>

      <main className="app-content">
        {activeTab === 'chat' && <ChatWindow />}
        {activeTab === 'analysis' && <AnalysisPanel />}
      </main>
    </div>
  )
}

export default App
