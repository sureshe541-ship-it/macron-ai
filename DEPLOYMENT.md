# Macron AI - Deployment Guide

## 🌐 Replit Deployment

This application is configured for deployment on Replit. Follow these steps:

### Prerequisites
- Replit account
- OpenAI API key

### Setup Steps

1. **Fork/Import Repository**
   - Import this repository to your Replit workspace
   - Or fork it on GitHub and import from GitHub

2. **Add Secrets**
   - Go to `Tools` → `Secrets`
   - Add `OPENAI_API_KEY` with your OpenAI API key

3. **Run Setup**
   ```bash
   bash setup.sh
   ```

4. **Start Application**
   - Click the "Run" button or run:
   ```bash
   pnpm dev
   ```

5. **Access Your App**
   - Backend API: `https://{your-replit-url}.replit.dev/api`
   - Frontend: `https://{your-replit-url}.replit.dev`
   - Health Check: `https://{your-replit-url}.replit.dev/api/health`

### Environment Variables

The application uses these environment variables:

```
OPENAI_API_KEY=your-api-key-here
OPENAI_MODEL=gpt-4
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=false (for production)
ALLOWED_ORIGINS=* (for Replit deployment)
FRONTEND_URL=your-replit-url
```

### Local Development (Non-Replit)

```bash
# Backend
cd backend
python main.py

# Frontend (in another terminal)
cd frontend
pnpm dev
```

### Docker Deployment

**Development:**
```bash
docker-compose up --build
```

**Production (Replit):**
```bash
docker-compose -f docker-compose.prod.yml up --build
```

## 🔐 Security Notes

- Never commit your `.env` file with real API keys
- Use Replit Secrets for sensitive data
- In production, set `DEBUG=false`
- Ensure CORS is properly configured for your domain

## 📊 API Endpoints

### Chat
- `POST /api/chat` - Send message to AI
- `GET /api/chat/{conversation_id}` - Get conversation history

### Analysis
- `POST /api/analyze` - Analyze text
- `GET /api/models` - Get available models

### Health
- `GET /api/health` - Health check
- `GET /` - Root endpoint

## 🆘 Troubleshooting

### Port Already in Use
- Replit automatically manages ports
- If issues persist, restart the Repl

### Dependencies Not Installing
```bash
pnpm install
pip install -r backend/requirements.txt
```

### API Connection Issues
- Check OPENAI_API_KEY is set
- Verify ALLOWED_ORIGINS includes your domain
- Check browser console for errors

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [OpenAI API Docs](https://platform.openai.com/docs/)
- [Replit Guide](https://docs.replit.com/)
