def infer_intent(message: str) -> str:
    text = message.lower()

    evaluator_keywords = ["error", "bug", "codigo", "revisa", "corrige", "funcion", "programa"]
    project_keywords = ["proyecto", "reto", "ejercicio", "practica", "challenge", "mini app"]

    if any(word in text for word in evaluator_keywords):
        return "evaluator"
    if any(word in text for word in project_keywords):
        return "project"
    return "mentor"