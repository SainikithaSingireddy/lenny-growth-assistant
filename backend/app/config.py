import os

class Settings:
    APP_NAME = "Lenny Growth Assistant"

    DATABASE_URL = os.getenv("DATABASE_URL")

    DEFAULT_PROVIDER = os.getenv("DEFAULT_PROVIDER", "openai")

    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:3b")
    OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

settings = Settings()