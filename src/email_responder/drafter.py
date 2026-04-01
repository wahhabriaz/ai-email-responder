from email_responder import settings
from email_responder.providers import get_client
from email_responder.logger import get_logger

log = get_logger(__name__)

TONES = {
    "professional": "formal, polished, and business-appropriate",
    "friendly":     "warm, approachable, and conversational",
    "concise":      "brief, direct, and to the point",
    "apologetic":   "empathetic, sincere, and solution-focused",
}


def draft_reply(
    original_email: str,
    context: str = "",
    tone: str | None = None,
) -> str:
    tone_desc = TONES.get(tone or settings.tone, TONES["professional"])
    prompt = f"""You are an expert email writer. Draft a reply to the email below.

Tone: {tone_desc}
Additional context: {context or 'None'}

Original email:
---
{original_email}
---

Write only the email body. No subject line. No preamble."""

    client = get_client()
    p = settings.provider.lower()

    if p == "anthropic":
        msg = client.messages.create(
            model=settings.model,
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}],
        )
        return msg.content[0].text
    elif p in ("openai", "groq", "ollama"):
        msg = client.chat.completions.create(
            model=settings.model,
            messages=[{"role": "user", "content": prompt}],
        )
        return msg.choices[0].message.content
    else:
        raise ValueError(f"Unknown provider: {p}")