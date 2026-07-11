"""
Macron AI - Main FastAPI application
Real AI-powered backend with LLM integration
"""

from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import os
from dotenv import load_dotenv
import logging

from services.llm_service import LLMService
from services.chat_service import ChatService
from models.conversation import Message, Conversation

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Macron AI",
    description="Real AI-powered API",
    version="1.0.0"
)

# Add CORS middleware
origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
llm_service = LLMService()
chat_service = ChatService(llm_service)


# Request/Response Models
class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[str] = None
    context: Optional[str] = None


class ChatResponse(BaseModel):
    response: str
    conversation_id: str
    message_id: str


class AnalysisRequest(BaseModel):
    text: str
    analysis_type: str = "general"  # general, sentiment, summary, entities


class AnalysisResponse(BaseModel):
    analysis: dict
    metadata: dict


# Health Check
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Macron AI",
        "version": "1.0.0"
    }


# Chat Endpoints
@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Main chat endpoint - send a message and get AI response
    """
    try:
        response = await chat_service.process_message(
            message=request.message,
            conversation_id=request.conversation_id,
            context=request.context
        )
        return response
    except Exception as e:
        logger.error(f"Chat error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/chat/{conversation_id}")
async def get_conversation(conversation_id: str):
    """Retrieve conversation history"""
    try:
        conversation = await chat_service.get_conversation(conversation_id)
        return conversation
    except Exception as e:
        logger.error(f"Get conversation error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


# Analysis Endpoints
@app.post("/api/analyze", response_model=AnalysisResponse)
async def analyze_text(request: AnalysisRequest):
    """
    Analyze text with different analysis types
    - general: comprehensive analysis
    - sentiment: sentiment analysis
    - summary: text summarization
    - entities: named entity recognition
    """
    try:
        analysis = await llm_service.analyze_text(
            text=request.text,
            analysis_type=request.analysis_type
        )
        return analysis
    except Exception as e:
        logger.error(f"Analysis error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


# Models Endpoint
@app.get("/api/models")
async def get_available_models():
    """Get list of available models"""
    try:
        models = await llm_service.get_available_models()
        return {"models": models}
    except Exception as e:
        logger.error(f"Models error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


# Error Handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {
        "error": exc.detail,
        "status_code": exc.status_code
    }


if __name__ == "__main__":
    import uvicorn
    
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", 8000))
    debug = os.getenv("DEBUG", "true").lower() == "true"
    
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=debug
    )
