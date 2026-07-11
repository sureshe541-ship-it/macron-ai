"""
Data models for conversations and messages
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class Message(BaseModel):
    """Message model"""
    id: str
    role: str  # user or assistant
    content: str
    timestamp: datetime = Field(default_factory=datetime.now)
    metadata: Optional[dict] = None


class Conversation(BaseModel):
    """Conversation model"""
    id: str
    messages: List[Message] = []
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    metadata: Optional[dict] = None
    
    def add_message(self, message: Message):
        """Add a message to conversation"""
        self.messages.append(message)
        self.updated_at = datetime.now()
    
    def get_last_message(self) -> Optional[Message]:
        """Get the last message in conversation"""
        return self.messages[-1] if self.messages else None


class ConversationThread(BaseModel):
    """Multiple conversations thread"""
    id: str
    conversations: List[Conversation] = []
    created_at: datetime = Field(default_factory=datetime.now)
