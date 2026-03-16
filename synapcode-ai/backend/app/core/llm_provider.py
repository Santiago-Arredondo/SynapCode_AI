import google.generativeai as genai

from app.core.config import settings

if settings.gemini_api_key:
    genai.configure(api_key=settings.gemini_api_key)


def generate_text(prompt: str) -> str:
    if not settings.gemini_api_key:
        return "Modo demo: no hay API key configurada."

    model = genai.GenerativeModel(settings.gemini_model)
    response = model.generate_content(prompt)
    return response.text if hasattr(response, "text") else "Error generando contenido."
