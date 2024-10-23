from toolhouse import Toolhouse
import os

def toolhouse_client(api_key: str | None = os.getenv("TOOLHOUSE_API_KEY"), provider: str = "openai") -> Toolhouse:
    if not api_key:
        raise ValueError("API key is required to create Toolhouse client")
    return Toolhouse(provider=provider, api_key=api_key)
