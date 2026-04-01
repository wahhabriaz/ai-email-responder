from email_responder import settings


def get_client():
    p = settings.provider.lower()
    if p == "anthropic":
        import anthropic
        return anthropic.Anthropic(api_key=settings.anthropic_api_key)
    elif p == "openai":
        import openai
        return openai.OpenAI(api_key=settings.openai_api_key)
    elif p == "groq":
        from groq import Groq
        return Groq(api_key=settings.groq_api_key)
    elif p == "ollama":
        import openai
        return openai.OpenAI(
            base_url=f"{settings.ollama_base_url}/v1",
            api_key="ollama",
        )
    else:
        raise ValueError(f"Unknown provider: {p}")