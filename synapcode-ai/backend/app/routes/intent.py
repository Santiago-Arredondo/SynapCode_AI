from fastapi import APIRouter

from app.schemas.intent import IntentRequest, IntentResponse
from app.services.intent_service import detect_intent

router = APIRouter(prefix="/intent", tags=["intent"])

@router.post("/", response_model=IntentResponse)
def intent(payload: IntentRequest):
    return IntentResponse(intent=detect_intent(payload.message))
