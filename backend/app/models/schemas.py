from pydantic import BaseModel
from typing import List
from datetime import datetime

class MessageCreate(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    session_id: int
    message: str
    provider: str = "ollama"


class MessageResponse(BaseModel):
    id: int
    role: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True


class SessionResponse(BaseModel):
    id: int
    title: str
    created_at: datetime

    class Config:
        from_attributes = True