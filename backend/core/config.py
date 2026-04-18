from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "AI Lead Agent"
    DEBUG: bool = True
    API_PREFIX: str = "/api"

    # add later
    OPENAI_API_KEY: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()