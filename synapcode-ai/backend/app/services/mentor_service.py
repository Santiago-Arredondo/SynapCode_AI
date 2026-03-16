<<<<<<< HEAD
from app.core.llm_provider import generate_with_gemini

def build_mentor_prompt(message: str, level: str, goal: str, topic: str | None = None) -> str:
    topic_block = f"Tema: {topic}\n" if topic else ""
    return f"""
Eres Mentor AI de SynapCode AI.

Responde siempre en español claro y natural para usuarios hispanohablantes.
Tu trabajo es enseñar programación e inteligencia artificial paso a paso.

Contexto:
- Nivel del estudiante: {level}
- Objetivo: {goal}

Reglas:
1. Explica de forma clara.
2. Adapta la explicación al nivel del estudiante.
3. Usa ejemplos sencillos.
4. Termina con una siguiente acción o mini ejercicio.
5. Mantén un tono cercano y profesional.

{topic_block}
Pregunta del estudiante:
{message}
""".strip()

def get_mentor_response(message: str, level: str, goal: str, topic: str | None = None) -> str:
    prompt = build_mentor_prompt(message, level, goal, topic)
    return generate_with_gemini(prompt)
=======
from app.core.llm_provider import generate_text
from app.models import MentorRequest


def generate_mentor_response(payload):
    prompt = (
        f"Eres un mentor AI. Nivel={payload.level}, objetivo={payload.goal}, tema={payload.topic}\n"
        f"Pregunta: {payload.message}\n"
    )
    return generate_text(prompt)
>>>>>>> 895b90f (Initial project structure for SynapCode AI)
