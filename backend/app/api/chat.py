from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.db_models import Message
from app.models.schemas import ChatRequest
from app.rag.retriever import retrieve_context
from app.providers.ollama_provider import OllamaProvider
from app.skills.artifact_generator import generate_html

router = APIRouter(prefix="/chat", tags=["Chat"])

provider = OllamaProvider()


@router.post("/")
async def chat(payload: ChatRequest, db: AsyncSession = Depends(get_db)):

    context = retrieve_context(payload.message)

    prompt = f"""
You are The Lenny Growth Assistant.

RULES:
- Answer ONLY from the transcript.
- If information is missing, say:
  "The transcript does not contain this information."
- Mention the source.

TRANSCRIPT:
{context}

QUESTION:
{payload.message}
"""

    answer = await provider.generate(prompt)

    db.add(
        Message(
            session_id=payload.session_id,
            role="user",
            content=payload.message,
        )
    )

    db.add(
        Message(
            session_id=payload.session_id,
            role="assistant",
            content=answer,
        )
    )

    await db.commit()

    artifact = generate_html(
        "Growth Insight",
        answer.replace("\n", "<br>")
    )

    return {
        "answer": answer,
        "artifact_html": artifact,
        "source": "Transcript",
        "context_used": True
    }