from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models.db_models import ChatSession

router = APIRouter(prefix="/sessions", tags=["Sessions"])


@router.post("/")
async def create_session(db: AsyncSession = Depends(get_db)):
    session = ChatSession(title="New Chat")
    db.add(session)
    await db.commit()
    await db.refresh(session)

    return {
        "id": session.id,
        "title": session.title,
        "created_at": session.created_at
    }


@router.get("/")
async def list_sessions(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ChatSession))
    sessions = result.scalars().all()

    return sessions