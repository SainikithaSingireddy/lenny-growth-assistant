from pathlib import Path

TRANSCRIPT_DIR = Path(__file__).resolve().parents[2] / "agent_transcripts"
TRANSCRIPT_DIR.mkdir(exist_ok=True)

sample = """Episode: Airbnb Growth

Lenny: Today we discuss how Airbnb improved onboarding.

Guest: The team reduced friction during signup, simplified forms,
and focused on activation metrics rather than registrations.
"""

(TRANSCRIPT_DIR / "airbnb_growth.md").write_text(sample, encoding="utf-8")

print("Transcript created successfully.")