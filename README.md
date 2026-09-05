# Lenny Growth Assistant

An enterprise-grade Retrieval-Augmented Generation (RAG) assistant that answers questions from **Lenny’s Podcast** transcripts using semantic search and grounded AI responses.

The application retrieves the most relevant transcript chunks from PostgreSQL + pgvector and generates source-attributed answers using configurable LLM providers.

---

## Live Demo

**Frontend:** https://lenny-growth-assistant-production-b353.up.railway.app

---

## Project Architecture

| Layer | Technology |
|--------|------------|
| Frontend | Next.js + TypeScript |
| Backend | FastAPI |
| Database | PostgreSQL + pgvector |
| Vector Search | pgvector (384 dimensions) |
| Embeddings | Sentence Transformers |
| LLM (Local) | Ollama (Llama 3.2) |
| LLM (Production) | Gemini 2.5 Flash |
| Frontend Hosting | Railway |
| Backend Hosting | Render |

---

## Features

- RAG-powered question answering
- Semantic transcript retrieval using pgvector
- Source-grounded responses
- Session-based chat interface
- HTML Artifact generation
- Configurable LLM provider (Ollama / Gemini)
- Production-ready cloud deployment

---

## Folder Structure

```text
lenny-growth-assistant/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── providers/
│   │   ├── rag/
│   │   ├── database.py
│   │   ├── config.py
│   │   └── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   └── lib/
│   └── package.json
│
├── agent_transcripts/
├── docs/
└── README.md
```

---

## How It Works

1. User submits a question.
2. FastAPI retrieves relevant transcript chunks using pgvector.
3. Retrieved context is sent to the selected LLM.
4. The model generates a grounded answer.
5. The application returns:
   - Chat response
   - Source filename
   - HTML artifact report

---

## Environment Variables

### Backend (.env)

```env
DATABASE_URL=your_postgresql_url

DEFAULT_PROVIDER=ollama

OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2:3b

GEMINI_API_KEY=your_gemini_api_key
```

### Render (Production)

```env
DATABASE_URL=<Render PostgreSQL URL>
DEFAULT_PROVIDER=gemini
GEMINI_API_KEY=<Gemini API Key>
```

### Railway (Frontend)

```env
NEXT_PUBLIC_API_URL=https://lenny-growth-assistant-backend.onrender.com
```

---

## Run Locally

### 1. Clone Repository

```bash
git clone https://github.com/SainikithaSingireddy/lenny-growth-assistant.git
cd lenny-growth-assistant
```

### 2. Backend

```bash
cd backend

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt

python -m uvicorn app.main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

### 3. Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```text
http://localhost:3000
```

---

## Deployment

### Frontend

- Platform: Railway
- Framework: Next.js
- Root Directory: `frontend`

### Backend

- Platform: Render
- Runtime: Python 3.11
- Start Command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

### Database

- Render PostgreSQL
- pgvector enabled
- Async SQLAlchemy + asyncpg

---

## API

### POST `/chat/`

**Request**

```json
{
  "message": "How did Airbnb improve onboarding?"
}
```

**Response**

```json
{
  "answer": "Airbnb reduced signup friction and focused on activation metrics.",
  "source": "airbnb_growth.md",
  "context_used": true,
  "artifact": "<html>...</html>"
}
```

---

## Example Questions

- How did Airbnb improve onboarding?
- What activation metrics did the guest recommend?
- How did the team reduce signup friction?
- What growth experiment was discussed?

---

## Tech Stack

- Next.js
- React
- TypeScript
- FastAPI
- SQLAlchemy
- PostgreSQL
- pgvector
- Sentence Transformers
- Ollama
- Gemini API
- Railway
- Render

---

## Notes

This project supports two LLM providers:

| Environment | Provider |
|------------|----------|
| Local Development | Ollama |
| Production Deployment | Gemini |

The provider is selected using the `DEFAULT_PROVIDER` environment variable, allowing the same codebase to run locally with Ollama and in production with Gemini.

---

## Author

**Sainikitha Singireddy**

Computer Science Graduate | Full Stack & Generative AI Developer

GitHub: https://github.com/SainikithaSingireddy