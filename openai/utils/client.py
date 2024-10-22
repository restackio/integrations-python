import os
from openai import OpenAI

openai_instance: OpenAI | None = None

def openai_client(api_key: str | None = os.getenv("OPENAI_API_KEY")) -> OpenAI:
    if not api_key:
        raise ValueError("API key is required to create OpenAI client")
    if not openai_instance:
        openai_instance = OpenAI(api_key=api_key)
    return openai_instance
