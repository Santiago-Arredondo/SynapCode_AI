import google.generativeai as genai
from app.core.config import GEMINI_API_KEY, GEMINI_MODEL

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def generate_with_gemini(prompt: str) -> str:
    if not GEMINI_API_KEY:
        return "Modo demo activo. Configura GEMINI_API_KEY."

    model = genai.GenerativeModel(GEMINI_MODEL)
    response = model.generate_content(prompt)
    return response.text if hasattr(response, "text") else "No se pudo generar respuesta."