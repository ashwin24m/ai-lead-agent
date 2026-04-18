from fastapi import APIRouter
from services.llm_service import generate_response

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/chat")
def chat(prompt: str):
    response = generate_response(prompt)
    return {"response": response}