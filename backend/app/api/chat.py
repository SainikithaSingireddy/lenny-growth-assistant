from fastapi import APIRouter

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/")
async def chat(payload: dict):
    return {
        "answer": f"You asked: {payload['message']}",
        "provider": payload.get("provider", "ollama")
    }