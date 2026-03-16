from app.core.llm_provider import generate_text
from app.models import MentorRequest


def generate_mentor_response(payload):
    prompt = (
        f"Eres un mentor AI. Nivel={payload.level}, objetivo={payload.goal}, tema={payload.topic}\n"
        f"Pregunta: {payload.message}\n"
    )
    return generate_text(prompt)
