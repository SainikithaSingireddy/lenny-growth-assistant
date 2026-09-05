import ollama
from app.config import settings
from app.providers.base import LLMProvider

class OllamaProvider(LLMProvider):

    async def generate(self, prompt: str):
        response = ollama.chat(
            model=settings.OLLAMA_MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response["message"]["content"]