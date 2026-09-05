from pathlib import Path

TRANSCRIPT_DIR = Path(__file__).resolve().parents[3] / "agent_transcripts"

def retrieve_context(question: str):
    context = []

    for file in TRANSCRIPT_DIR.glob("*.md"):
        text = file.read_text(encoding="utf-8")
        if any(word.lower() in text.lower() for word in question.split()):
            context.append(f"Source: {file.name}\n{text}")

    if not context:
        return "No matching transcript found."

    return "\n\n".join(context)