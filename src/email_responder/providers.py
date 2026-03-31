import anthropic
import openai
from groq import Groq
from email_responder import settings


def get_client():
    p = settings.provider.lower()
    if p == "anthropic":
        return anthropic.Anthropic(api_key=settings.anthropic_api_key)
    elif p == "openai":
        return openai.OpenAI(api_key=settings.openai_api_key)
    elif p == "groq":
        return Groq(api_key=settings.groq_api_key)
    else:
        raise ValueError(f"Unknown provider: {p}")