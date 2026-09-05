from pathlib import Path

TRANSCRIPT_DIR = Path(__file__).resolve().parents[2] / "agent_transcripts"

for file in TRANSCRIPT_DIR.glob("*.md"):
    text = file.read_text(encoding="utf-8")
    print(f"Ingested: {file.name}")
    print(text[:120])