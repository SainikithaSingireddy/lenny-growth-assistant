
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    APP_NAME: str = "Lenny Growth Assistant"

    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql+asyncpg://postgres:password@localhost:5432/lenny_db"
    )

    DEFAULT_PROVIDER: str = os.getenv("DEFAULT_PROVIDER", "ollama")

    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "llama3.2:3b")
    OLLAMA_URL: str = os.getenv("OLLAMA_URL", "http://localhost:11434")

settings = Settings()