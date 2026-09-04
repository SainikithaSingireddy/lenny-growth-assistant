# Architecture Specification

# The Lenny Growth Assistant

## High-Level Architecture

User → Next.js Frontend → FastAPI Backend → RAG Retriever → PostgreSQL + pgvector → Ollama/OpenAI

## Components

### Frontend
- Next.js (React)
- Tailwind CSS
- Chat interface
- Artifact Viewer
- Provider selector

### Backend
- FastAPI REST API
- Session management
- Chat endpoint
- Health endpoint

### Database
PostgreSQL stores:
- Chat sessions
- Messages
- Transcript metadata
- Vector embeddings

pgvector performs semantic similarity search.

### AI Layer

Embedding Model:
- sentence-transformers (MiniLM)

LLM Providers:
- Ollama (Local)
- OpenAI (Cloud)

The provider is selected dynamically using configuration.

## API Endpoints

POST /api/sessions
Creates a new chat session.

GET /api/sessions/{id}
Returns previous messages.

POST /api/chat
Receives user question and streams response.

GET /api/health
Checks database and model availability.

## Retrieval Flow

1. User sends question.
2. Generate embedding.
3. Search pgvector.
4. Retrieve top transcript chunks.
5. Build grounded prompt.
6. LLM generates cited answer.
7. Stream response to frontend.

## Security

- HTML rendered inside sandboxed iframe
- Environment variables stored in .env
- No API keys committed to Git

## Deployment

Docker Compose starts:
- PostgreSQL
- FastAPI
- Next.js
- Optional Ollama