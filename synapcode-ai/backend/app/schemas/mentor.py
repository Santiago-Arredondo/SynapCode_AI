from pydantic import BaseModel, Field
from typing import Optional, Literal

class MentorRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=4000)
    level: Literal["principiante", "basico", "intermedio", "avanzado"] = "principiante"
    goal: Optional[str] = "Aprender desarrollo de software e inteligencia artificial"
    topic: Optional[str] = None

class MentorResponse(BaseModel):
    response: str
    agent: str = "mentor_ai"
    language: str = "es"
    provider: str = "gemini"
