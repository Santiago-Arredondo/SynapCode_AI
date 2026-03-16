from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional, Literal

from app.services.mentor_service import get_mentor_response
from app.services.intent_service import infer_intent
from app.core.config import GEMINI_API_KEY

app = FastAPI(title="SynapCode AI MVP API", version="0.1.0")


class MentorRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=4000)
    level: Literal["principiante", "basico", "intermedio", "avanzado"] = "principiante"
    goal: Optional[str] = "Aprender desarrollo de software e inteligencia artificial"
    topic: Optional[str] = None


class IntentRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=4000)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "synapcode-mvp-api",
        "provider": "gemini" if GEMINI_API_KEY else "demo",
    }


@app.post("/intent")
def detect_intent(payload: IntentRequest):
    return {"intent": infer_intent(payload.message)}


@app.post("/mentor/chat")
def mentor_chat(payload: MentorRequest):
    response = get_mentor_response(
        message=payload.message,
        level=payload.level,
        goal=payload.goal,
        topic=payload.topic,
    )
    return {
        "agent": "mentor_ai",
        "language": "es",
        "response": response,
    }