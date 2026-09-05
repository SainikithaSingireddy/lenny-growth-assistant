from fastapi import APIRouter
from app.rag.retriever import retrieve_context
from app.providers.ollama_provider import OllamaProvider
from app.providers.gemini_provider import GeminiProvider
from app.config import settings

router = APIRouter(prefix="/chat", tags=["Chat"])

provider = (
    GeminiProvider()
    if settings.DEFAULT_PROVIDER == "gemini"
    else OllamaProvider()
)

@router.post("/")
async def chat(payload: dict):
    context = retrieve_context(payload["message"])

    prompt = f"""
You are The Lenny Growth Assistant.

RULES:
- Answer ONLY from the transcript below.
- If the answer is not present, say exactly:
  "The transcript does not contain this information."
- Mention the source filename.

TRANSCRIPT:
{context}

QUESTION:
{payload["message"]}
"""

    answer = await provider.generate(prompt)

    return {
        "answer": answer,
        "source": "agent_transcripts",
        "context_used": True
    }