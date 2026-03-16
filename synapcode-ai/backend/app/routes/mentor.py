from fastapi import APIRouter

from app.schemas.mentor import MentorRequest, MentorResponse
from app.services.mentor_service import generate_mentor_response

router = APIRouter(prefix="/mentor", tags=["mentor"])

@router.post("/chat", response_model=MentorResponse)
def mentor_chat(payload: MentorRequest):
    answer = generate_mentor_response(payload)
    return MentorResponse(response=answer, agent="mentor_ai", language="es", provider="gemini")
