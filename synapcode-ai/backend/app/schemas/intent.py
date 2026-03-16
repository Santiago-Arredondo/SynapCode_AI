from pydantic import BaseModel, Field
from typing import Literal

class IntentRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=4000)

class IntentResponse(BaseModel):
    intent: Literal["mentor", "evaluator", "project"]
