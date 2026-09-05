from fastapi import APIRouter
from app.rag.retriever import retrieve_context
from app.providers.ollama_provider import OllamaProvider
from app.providers.gemini_provider import GeminiProvider
from app.config import settings

router = APIRouter(prefix="/chat", tags=["Chat"])

provider = GeminiProvider() if settings.DEFAULT_PROVIDER == "gemini" else OllamaProvider()

@router.post("/")
async def chat(payload: dict):
    question = payload["message"]
    context = retrieve_context(question)

    prompt = f"""
You are The Lenny Growth Assistant.

Answer ONLY using the transcript below.

TRANSCRIPT:
{context}

QUESTION:
{question}
"""

    answer = await provider.generate(prompt)

    artifact = f"""
    <div style='font-family:Arial;padding:24px'>
        <h1>Lenny Growth Assistant</h1>
        <h2>Question</h2>
        <p>{question}</p>
        <h2>Answer</h2>
        <p>{answer}</p>
        <hr>
        <b>Source:</b> airbnb_growth.md
    </div>
    """

    return {
        "answer": answer,
        "source": "airbnb_growth.md",
        "context_used": True,
        "artifact": artifact
    }