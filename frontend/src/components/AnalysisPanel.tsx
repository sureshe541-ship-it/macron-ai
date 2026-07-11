import { useState } from 'react'
import { apiClient } from '../utils/api'
import '../styles/AnalysisPanel.css'

type AnalysisType = 'general' | 'sentiment' | 'summary' | 'entities'

export default function AnalysisPanel() {
  const [text, setText] = useState('')
  const [analysisType, setAnalysisType] = useState<AnalysisType>('general')
  const [result, setResult] = useState<any>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const handleAnalyze = async (e: React.FormEvent) => {
    e.preventDefault()
    
    if (!text.trim()) {
      setError('Please enter text to analyze')
      return
    }

    setLoading(true)
    setError('')
    setResult(null)

    try {
      const response = await apiClient.post('/api/analyze', {
        text: text,
        analysis_type: analysisType
      })
      setResult(response.data)
    } catch (err) {
      setError('Failed to analyze text. Please try again.')
      console.error('Analysis error:', err)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="analysis-panel">
      <div className="analysis-header">
        <h2>Text Analysis Tool</h2>
        <p>Analyze text with different analysis types</p>
      </div>

      <form onSubmit={handleAnalyze} className="analysis-form">
        <div className="form-group">
          <label htmlFor="text">Text to Analyze</label>
          <textarea
            id="text"
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Enter text for analysis..."
            rows={6}
            disabled={loading}
            className="analysis-textarea"
          />
        </div>

        <div className="form-group">
          <label htmlFor="type">Analysis Type</label>
          <select
            id="type"
            value={analysisType}
            onChange={(e) => setAnalysisType(e.target.value as AnalysisType)}
            disabled={loading}
            className="analysis-select"
          >
            <option value="general">General Analysis</option>
            <option value="sentiment">Sentiment Analysis</option>
            <option value="summary">Summarization</option>
            <option value="entities">Entity Extraction</option>
          </select>
        </div>

        {error && <div className="error-message">{error}</div>}

        <button 
          type="submit" 
          disabled={loading || !text.trim()}
          className="analyze-btn"
        >
          {loading ? 'Analyzing...' : 'Analyze'}
        </button>
      </form>

      {result && (
        <div className="analysis-result">
          <h3>Analysis Result</h3>
          <div className="result-content">
            <pre>{JSON.stringify(result.analysis, null, 2)}</pre>
          </div>
          <div className="result-metadata">
            <small>
              Type: {result.metadata.analysis_type} | 
              Text length: {result.metadata.text_length} characters |
              Model: {result.metadata.model}
            </small>
          </div>
        </div>
      )}
    </div>
  )
}
