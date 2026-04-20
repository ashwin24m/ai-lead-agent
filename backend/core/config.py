from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "AI Lead Agent"
    DEBUG: bool = True
    API_PREFIX: str = "/api"

    OPENAI_API_KEY: str | None = None

    model_config = SettingsConfigDict(
        env_file="backend/.env"   
    )

settings = Settings()