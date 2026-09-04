# Product Requirements Document (PRD)

## Project

The Lenny Growth Assistant

## Problem Statement

Product managers and growth leaders often need insights from hundreds of hours of Lenny's Podcast interviews. Searching manually across transcripts is slow and unreliable.

The goal is to build an AI-powered assistant that retrieves grounded answers directly from podcast transcripts, generates long-form content, and renders rich artifacts inside the application.

## Primary User

- Product Managers
- Growth Leaders
- Startup Founders
- Designers researching product strategy

## User Goals

1. Ask questions in natural language.
2. Receive source-grounded answers.
3. Generate Ship 30 style essays.
4. Export Markdown or HTML artifacts.

## Success Metrics

- Citation accuracy above 90%
- Response begins within 4 seconds using local Ollama
- Every answer includes transcript source attribution
- Users can switch between Ollama and OpenAI without code changes

## Assumptions

- The transcript repository is available locally.
- Users trust only cited responses.
- Local inference is preferred during evaluation.

## Scope Included

- RAG chatbot
- Session history
- PostgreSQL persistence
- Artifact Viewer
- Ollama + OpenAI support

## Out of Scope

- User authentication
- Multi-user collaboration
- Voice input
- Mobile application

## Risks

- Hallucinated responses
- Slow local inference
- Incorrect retrieval
- Unsafe HTML rendering

## Acceptance Criteria

- Users can start a chat.
- Questions retrieve relevant transcript chunks.
- Answers contain citations.
- Ship30 essays are generated.
- HTML artifacts render safely.
- Docker starts the complete system with one command.