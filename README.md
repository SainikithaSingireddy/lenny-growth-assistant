# Lenny Growth Assistant

**Enterprise Retrieval-Augmented Generation (RAG) Assistant** built with **FastAPI, PostgreSQL + pgvector, Ollama, and Next.js**.

## Overview

Lenny Growth Assistant is a full-stack AI application that enables users to ask natural-language questions about podcast transcripts and receive **grounded, source-attributed answers**.

The system uses a Retrieval-Augmented Generation (RAG) pipeline with semantic search using **pgvector** and local LLM inference through **Ollama**.

> **Note:** This submission includes a sample transcript (Airbnb Growth) to demonstrate the complete RAG workflow. The ingestion pipeline is designed to scale to multiple podcast transcripts.

## Features

* Semantic transcript retrieval using **pgvector**
* FastAPI REST backend
* Next.js + TypeScript frontend
* PostgreSQL database with vector embeddings
* Ollama local LLM integration
* Session-based conversations
* Source-grounded AI responses
* HTML Artifact Viewer
* Modular provider architecture

## Tech Stack

### Frontend

* Next.js
* React
* TypeScript

### Backend

* FastAPI
* SQLAlchemy
* PostgreSQL
* pgvector

### AI Stack

* Ollama (Llama 3.2)
* Sentence Transformers
* Retrieval-Augmented Generation (RAG)

## Architecture

```text
                Next.js Frontend
                       │
                       ▼
                 FastAPI Backend
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
   Session API     Retriever      Artifact Generator
                       │
                       ▼
            PostgreSQL + pgvector
                       │
                       ▼
                  Ollama (LLM)
```

## Project Structure

```text
lenny-growth-assistant/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── providers/
│   │   ├── rag/
│   │   └── skills/
│   ├── scripts/
│   ├── tests/
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   ├── hooks/
│   │   └── lib/
│   └── package.json
│
├── docs/
├── docker-compose.yml
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/SainikithaSingireddy/lenny-growth-assistant.git

cd lenny-growth-assistant
```

### 2. Start PostgreSQL

```bash
docker compose up -d
```

### 3. Run Backend

```bash
cd backend

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

python -m uvicorn app.main:app --reload
```

Backend URL:

`http://127.0.0.1:8000`

Swagger Documentation:

`http://127.0.0.1:8000/docs`

### 4. Run Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend URL:

`http://localhost:3000`

## How RAG Works

1. User enters a question.
2. The retriever searches transcript chunks using **pgvector** similarity.
3. Relevant transcript context is retrieved.
4. Ollama generates an answer using only the retrieved context.
5. The response includes source attribution and an HTML artifact preview.

## Example Questions

* How did Airbnb improve onboarding?
* What activation metrics did the guest recommend?
* How did the team reduce signup friction?
* What did the transcript say about user activation?

## API Endpoints

| Method | Endpoint     | Description    |
| ------ | ------------ | -------------- |
| GET    | `/health`    | Health check   |
| POST   | `/chat/`     | Ask a question |
| GET    | `/sessions/` | List sessions  |
| POST   | `/sessions/` | Create session |

## Demo Workflow

1. Start Docker
2. Launch FastAPI
3. Launch Next.js
4. Open `localhost:3000`
5. Ask a transcript-related question
6. View grounded answer and HTML artifact

## Future Improvements

* Multi-episode transcript ingestion
* Streaming LLM responses
* Multiple provider support (OpenAI/Ollama)
* Advanced conversation history
* Cloud deployment for backend

## Author

**Sainikitha Singireddy**

B.Tech Computer Science & Engineering
