from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.llm_service import generate_response
from backend.agent.tools.lead_extractor import extract_lead_info

# ✅ router must be defined BEFORE usage
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


@router.post("/extract")
def extract(request: ChatRequest):
    data = extract_lead_info(request.prompt)
    return {"lead_data": data}