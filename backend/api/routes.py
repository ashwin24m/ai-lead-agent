from fastapi import APIRouter
from core.logger import logger

router = APIRouter()

@router.get("/health")
def health_check():
    logger.info("Health check called")
    return {"status": "ok"}

@router.get("/")
def root():
    return {"message": "AI Lead Agent API is running"}