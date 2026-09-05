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
    question = payload["message"]
    context = retrieve_context(question)

    prompt = f"""
You are The Lenny Growth Assistant.

RULES:
- Answer ONLY from the transcript below.
- If the answer is not present, say exactly:
  "The transcript does not contain this information."

TRANSCRIPT:
{context}

QUESTION:
{question}
"""

    answer = await provider.generate(prompt)

    artifact = f"""
    <div style="font-family:Arial;padding:24px">
      <h1 style="color:#2563eb;">Lenny Growth Assistant</h1>

      <h2>Question</h2>
      <p>{question}</p>

      <h2>Answer</h2>
      <p>{answer}</p>

      <hr/>

      <h3>Source</h3>
      <p>airbnb_growth.md</p>
    </div>
    """

    return {
        "answer": answer,
        "source": "airbnb_growth.md",
        "context_used": True,
        "artifact": artifact
    }