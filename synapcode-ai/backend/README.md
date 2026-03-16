# SynapCode AI Backend

Servicios FastAPI para mentor, intenciona y ejercicios.

## setup

1. crear y activar virtualenv
2. pip install -r requirements.txt
3. cp .env.example .env (en este caso solo backend/.env)
4. setear GEMINI_API_KEY con la clave de Google Gemini

## ejecutar

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
