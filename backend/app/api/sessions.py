from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.db_models import ChatSession

router = APIRouter(prefix="/sessions", tags=["Sessions"])

@router.get("/")
async def get_sessions(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ChatSession))
    sessions = result.scalars().all()

    return [
        {
            "id": s.id,
            "title": s.title
        }
        for s in sessions
    ]


@router.post("/")
async def create_session(db: AsyncSession = Depends(get_db)):
    session = ChatSession(title="New Conversation")

    db.add(session)
    await db.commit()
    await db.refresh(session)

    return {
        "id": session.id,
        "title": session.title
    }