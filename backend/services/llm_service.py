"""
LLM Service - Handles all interactions with Language Models
"""

import os
from typing import Optional, Dict, List, Any
from openai import AsyncOpenAI
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class LLMService:
    """Service for interacting with LLM APIs (OpenAI)"""
    
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("OPENAI_MODEL", "gpt-4")
        self.client = AsyncOpenAI(api_key=self.api_key)
        
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
    
    async def generate_response(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2000,
    ) -> str:
        """
        Generate a response from the LLM
        """
        try:
            messages = []
            
            if system_prompt:
                messages.append({
                    "role": "system",
                    "content": system_prompt
                })
            
            messages.append({
                "role": "user",
                "content": prompt
            })
            
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            logger.error(f"LLM generation error: {str(e)}")
            raise
    
    async def analyze_text(
        self,
        text: str,
        analysis_type: str = "general"
    ) -> Dict[str, Any]:
        """
        Analyze text based on analysis type
        """
        try:
            system_prompts = {
                "sentiment": "Analyze the sentiment of the text. Return: sentiment (positive/negative/neutral), score (0-1), explanation.",
                "summary": "Summarize the text concisely in 2-3 sentences.",
                "entities": "Extract named entities (people, places, organizations) from the text.",
                "general": "Provide a comprehensive analysis of this text covering: key points, tone, intent, and potential insights."
            }
            
            system_prompt = system_prompts.get(analysis_type, system_prompts["general"])
            
            response = await self.generate_response(
                prompt=text,
                system_prompt=system_prompt,
                temperature=0.5,
                max_tokens=1000
            )
            
            return {
                "analysis": {"content": response},
                "metadata": {
                    "analysis_type": analysis_type,
                    "timestamp": datetime.now().isoformat(),
                    "model": self.model,
                    "text_length": len(text)
                }
            }
        
        except Exception as e:
            logger.error(f"Text analysis error: {str(e)}")
            raise
    
    async def generate_summary(self, text: str) -> str:
        """Generate a summary of the text"""
        system_prompt = "You are a text summarization expert. Create a concise summary that captures the main ideas."
        return await self.generate_response(
            prompt=f"Please summarize this text:\n\n{text}",
            system_prompt=system_prompt,
            temperature=0.5,
            max_tokens=500
        )
    
    async def extract_entities(self, text: str) -> List[Dict[str, str]]:
        """Extract entities from text"""
        system_prompt = "Extract named entities (people, places, organizations, dates) from the text. Format as JSON array with entity and type."
        response = await self.generate_response(
            prompt=f"Extract entities from: {text}",
            system_prompt=system_prompt,
            temperature=0.3,
            max_tokens=500
        )
        return response
    
    async def get_available_models(self) -> List[str]:
        """Get list of available models (mock for now)"""
        return [
            "gpt-4",
            "gpt-3.5-turbo",
            "gpt-4-turbo-preview"
        ]
    
    async def stream_response(
        self,
        prompt: str,
        system_prompt: Optional[str] = None
    ):
        """
        Stream a response from the LLM
        """
        try:
            messages = []
            
            if system_prompt:
                messages.append({
                    "role": "system",
                    "content": system_prompt
                })
            
            messages.append({
                "role": "user",
                "content": prompt
            })
            
            stream = await self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                stream=True,
                temperature=0.7,
                max_tokens=2000
            )
            
            async for chunk in stream:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
        
        except Exception as e:
            logger.error(f"LLM stream error: {str(e)}")
            raise
