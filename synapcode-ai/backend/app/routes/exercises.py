from fastapi import APIRouter

router = APIRouter(prefix="/exercises", tags=["exercises"])

@router.get("/")
def list_exercises():
    return {"exercises": ["Ejercicio 1", "Ejercicio 2", "Ejercicio 3"]}
