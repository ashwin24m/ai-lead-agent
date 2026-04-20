from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.llm_service import generate_response

router = APIRouter()

class ChatRequest(BaseModel):
    prompt: str


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/chat")
def chat(request: ChatRequest):
    response = generate_response(request.prompt)
    return {"response": response}