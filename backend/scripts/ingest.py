from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.db_models import TranscriptChunk
from app.rag.embeddings import embed

DATABASE = "postgresql://postgres:password@localhost:5432/lenny_db"

engine = create_engine(DATABASE)

Session = sessionmaker(bind=engine)

ROOT = Path(__file__).resolve().parents[2]

TRANSCRIPTS = ROOT / "agent_transcripts"

db = Session()

for file in TRANSCRIPTS.glob("*.md"):

    text = file.read_text(encoding="utf-8")

    paragraphs = text.split("\n\n")

    for p in paragraphs:

        if len(p.strip()) < 20:
            continue

        db.add(
            TranscriptChunk(
                episode=file.stem,
                source=file.name,
                chunk=p,
                embedding=embed(p),
            )
        )

db.commit()

print("Ingestion complete")