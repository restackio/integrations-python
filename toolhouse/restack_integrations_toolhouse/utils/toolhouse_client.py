from toolhouse import Toolhouse
import os

def get_toolhouse_client(api_key: str | None = None, provider: str = "openai") -> Toolhouse:
    if api_key is None:
        api_key = os.environ.get('TOOLHOUSE_API_KEY')
    
    return Toolhouse(provider=provider, api_key=api_key)
