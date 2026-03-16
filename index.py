from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional, Literal
import os

import google.generativeai as genai

app = FastAPI(title="SynapCode AI MVP API", version="0.2.0")


# =========================
# Configuracion
# =========================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)


# =========================
# Schemas
# =========================
class HealthResponse(BaseModel):
    status: str
    service: str
    provider: str


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


class IntentRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=4000)


class IntentResponse(BaseModel):
    intent: Literal["mentor", "evaluator", "project"]


# =========================
# Prompts
# =========================
def build_mentor_prompt(level: str, goal: Optional[str], message: str, topic: Optional[str] = None) -> str:
    topic_block = f"Tema: {topic}\n" if topic else ""

    return f"""
Eres Mentor AI de SynapCode AI.

Responde siempre en espanol claro y natural para usuarios hispanohablantes.
Tu rol es ensenar desarrollo de software e inteligencia artificial paso a paso.

Contexto del estudiante:
- Nivel: {level}
- Objetivo: {goal}

Reglas:
1. Explica conceptos con claridad.
2. Adapta la explicacion al nivel del estudiante.
3. Usa ejemplos sencillos cuando sea util.
4. Si el tema es tecnico, da una explicacion y luego un ejemplo practico.
5. Termina con una siguiente accion o ejercicio corto.
6. Usa un tono cercano, claro y profesional.
7. Si hablas de codigo, usa buenas practicas y ejemplos pequenos.

{topic_block}
Pregunta del estudiante:
{message}
""".strip()


# =========================
# Helpers
# =========================
def infer_intent(message: str) -> str:
    text = message.lower()

    evaluator_keywords = ["error", "bug", "codigo", "revisa", "corrige", "funcion", "programa"]
    project_keywords = ["proyecto", "reto", "ejercicio", "practica", "challenge", "mini app"]

    if any(word in text for word in evaluator_keywords):
        return "evaluator"
    if any(word in text for word in project_keywords):
        return "project"
    return "mentor"


def call_gemini(prompt: str) -> str:
    if not GEMINI_API_KEY:
        return (
            "Modo demo activo. Aun no has configurado GEMINI_API_KEY. "
            "Agrega tu API key de Google AI Studio para obtener respuestas reales."
        )

    model = genai.GenerativeModel(GEMINI_MODEL)
    response = model.generate_content(prompt)
    return response.text if hasattr(response, "text") else "No se pudo generar respuesta."


# =========================
# Routes
# =========================
@app.get("/health", response_model=HealthResponse)
def health_check():
    return HealthResponse(
        status="ok",
        service="synapcode-mvp-api",
        provider="gemini" if GEMINI_API_KEY else "demo",
    )


@app.post("/intent", response_model=IntentResponse)
def detect_intent(payload: IntentRequest):
    intent = infer_intent(payload.message)
    return IntentResponse(intent=intent)


@app.post("/mentor/chat", response_model=MentorResponse)
def mentor_chat(payload: MentorRequest):
    prompt = build_mentor_prompt(payload.level, payload.goal, payload.message, payload.topic)
    response_text = call_gemini(prompt)
    return MentorResponse(response=response_text, provider="gemini" if GEMINI_API_KEY else "demo")


@app.get("/")
def root():
    return {
        "message": "Bienvenido a la API MVP de SynapCode AI",
        "docs": "/docs",
        "endpoints": ["/health", "/intent", "/mentor/chat"],
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
