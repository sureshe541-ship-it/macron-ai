# Macron AI - Real AI-Powered Application

A full-stack, production-ready AI application built with FastAPI, React, and OpenAI's GPT models.

## 🚀 Features

- **Interactive Chat Interface** - Real-time chat with AI assistant
- **Advanced Text Analysis** - Sentiment analysis, summarization, entity extraction
- **Scalable Backend** - FastAPI with async support
- **Modern Frontend** - React with TypeScript and Vite
- **Docker Support** - Easy deployment with Docker Compose
- **Responsive Design** - Mobile-friendly UI
- **API-First Architecture** - RESTful API with proper error handling

## 📋 Tech Stack

### Backend
- **FastAPI** - High-performance Python web framework
- **OpenAI API** - GPT-4 and GPT-3.5 integration
- **Pydantic** - Data validation and settings management
- **Uvicorn** - ASGI web server

### Frontend
- **React 18** - UI library
- **TypeScript** - Type-safe development
- **Vite** - Fast build tool
- **Zustand** - State management
- **Axios** - HTTP client

### Infrastructure
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration

## 🛠 Setup & Installation

### Prerequisites
- Python 3.11+
- Node.js 18+
- Docker & Docker Compose (optional)
- OpenAI API key

### Local Development

#### 1. Clone the repository
```bash
git clone <repository-url>
cd macron-ai
```

#### 2. Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# Run development server
python main.py
```

Backend will be available at `http://localhost:8000`

#### 3. Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

Frontend will be available at `http://localhost:3000`

### Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up --build

# Access the application
# Frontend: http://localhost:3000
# Backend: http://localhost:8000
```

## 📚 API Endpoints

### Chat
- `POST /api/chat` - Send a message and get AI response
- `GET /api/chat/{conversation_id}` - Get conversation history

### Analysis
- `POST /api/analyze` - Analyze text with different analysis types
- `GET /api/models` - Get available AI models

### Health
- `GET /health` - Health check endpoint

## 🧠 Analysis Types

1. **General** - Comprehensive text analysis
2. **Sentiment** - Sentiment analysis (positive/negative/neutral)
3. **Summary** - Text summarization
4. **Entities** - Named entity recognition

## 📁 Project Structure

```
macron-ai/
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── services/
│   │   ├── llm_service.py      # LLM integration
│   │   └── chat_service.py     # Chat logic
│   ├── models/
│   │   └── conversation.py     # Data models
│   ├── requirements.txt        # Python dependencies
│   ├── .env.example            # Environment template
│   └── Dockerfile              # Backend container
├── frontend/
│   ├── src/
│   │   ├── components/         # React components
│   │   ├── styles/            # CSS styles
│   │   ├── utils/             # Utilities
│   │   ├── store/             # Zustand stores
│   │   ├── App.tsx            # Main app
│   │   └── main.tsx           # Entry point
│   ├── package.json           # Node dependencies
│   ├── vite.config.ts         # Vite config
│   ├── tsconfig.json          # TypeScript config
│   ├── index.html             # HTML entry
│   └── Dockerfile             # Frontend container
├── docker-compose.yml         # Docker Compose config
└── README.md                  # This file
```

## 🔐 Environment Variables

### Backend (.env)
```
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=true
ALLOWED_ORIGINS=http://localhost:3000
FRONTEND_URL=http://localhost:3000
```

## 🎯 Usage

### Chat
1. Open frontend at `http://localhost:3000`
2. Type your message in the chat input
3. Get AI-powered responses in real-time
4. Chat history is maintained in the conversation

### Analysis
1. Navigate to the "Analysis" tab
2. Enter text to analyze
3. Select analysis type
4. View results

## 🚀 Deployment

### Production Build
```bash
# Frontend
npm run build

# Backend
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 main:app
```

### Docker Production
```bash
docker-compose -f docker-compose.yml up -d
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the MIT License.

## 🆘 Support

For issues and questions:
1. Check existing issues
2. Create a new issue with detailed information
3. Include steps to reproduce

## 🎓 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)

---

**Built with ❤️ for real AI applications**
