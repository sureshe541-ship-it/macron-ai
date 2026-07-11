"""
Chat Service - Manages conversation state and chat logic
"""

import uuid
from typing import Optional, Dict, List
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class ChatService:
    """Service for managing chat conversations"""
    
    def __init__(self, llm_service):
        self.llm_service = llm_service
        self.conversations: Dict[str, List[Dict]] = {}
    
    async def process_message(
        self,
        message: str,
        conversation_id: Optional[str] = None,
        context: Optional[str] = None
    ) -> Dict:
        """
        Process a message and return AI response
        """
        try:
            # Create or get conversation
            if not conversation_id:
                conversation_id = str(uuid.uuid4())
                self.conversations[conversation_id] = []
            
            # Build system prompt with context
            system_prompt = "You are a helpful and knowledgeable AI assistant."
            if context:
                system_prompt += f"\n\nAdditional context: {context}"
            
            # Generate response
            response = await self.llm_service.generate_response(
                prompt=message,
                system_prompt=system_prompt
            )
            
            # Store in conversation history
            message_id = str(uuid.uuid4())
            self.conversations[conversation_id].append({
                "id": message_id,
                "role": "user",
                "content": message,
                "timestamp": datetime.now().isoformat()
            })
            
            response_id = str(uuid.uuid4())
            self.conversations[conversation_id].append({
                "id": response_id,
                "role": "assistant",
                "content": response,
                "timestamp": datetime.now().isoformat()
            })
            
            return {
                "response": response,
                "conversation_id": conversation_id,
                "message_id": response_id
            }
        
        except Exception as e:
            logger.error(f"Chat processing error: {str(e)}")
            raise
    
    async def get_conversation(self, conversation_id: str) -> Dict:
        """Retrieve conversation history"""
        try:
            if conversation_id not in self.conversations:
                return {
                    "id": conversation_id,
                    "messages": [],
                    "created_at": datetime.now().isoformat()
                }
            
            messages = self.conversations[conversation_id]
            return {
                "id": conversation_id,
                "messages": messages,
                "message_count": len(messages),
                "created_at": messages[0]["timestamp"] if messages else datetime.now().isoformat()
            }
        
        except Exception as e:
            logger.error(f"Get conversation error: {str(e)}")
            raise
    
    def clear_conversation(self, conversation_id: str) -> bool:
        """Clear conversation history"""
        if conversation_id in self.conversations:
            del self.conversations[conversation_id]
            return True
        return False
    
    def get_all_conversations(self) -> List[str]:
        """Get all conversation IDs"""
        return list(self.conversations.keys())
