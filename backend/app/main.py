from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import Base, engine
from app.models.db_models import ChatSession, Message
from app.api.health import router as health_router
from app.api.sessions import router as session_router
from app.api.chat import router as chat_router

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="Oogway Labs Forward Deployed Engineer Assignment"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Lenny Growth Assistant Backend Running"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "provider": settings.DEFAULT_PROVIDER
    }

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(health_router)
app.include_router(session_router)
app.include_router(chat_router)