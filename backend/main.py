from fastapi import FastAPI
from core.config import settings
from api.routes import router
from core.logger import logger

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)

app.include_router(router, prefix=settings.API_PREFIX)

@app.on_event("startup")
def startup_event():
    logger.info("Starting AI Lead Agent...")

@app.on_event("shutdown")
def shutdown_event():
    logger.info("Shutting down AI Lead Agent...")