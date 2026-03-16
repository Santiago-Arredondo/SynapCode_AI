from fastapi import FastAPI

from app.routes import health, intent, mentor, exercises

app = FastAPI(title="SynapCode AI MVP API", version="0.2.0")

app.include_router(health.router)
app.include_router(intent.router)
app.include_router(mentor.router)
app.include_router(exercises.router)

@app.get("/")
def root():
    return {
        "message": "Bienvenido a SynapCode AI",
        "docs": "/docs",
        "endpoints": ["/health", "/intent", "/mentor", "/exercises"],
    }
