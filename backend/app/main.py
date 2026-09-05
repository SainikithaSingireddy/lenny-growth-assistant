from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.database import Base, engine
from app.api.chat import router as chat_router
from app.api.sessions import router as sessions_router

app = FastAPI(
    title="Lenny Growth Assistant",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(chat_router)
app.include_router(sessions_router)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        
        await conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))

        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def root():
    return {
        "message": "Lenny Growth Assistant API is running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }