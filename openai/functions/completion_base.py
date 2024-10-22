from restack_ai import Function
from openai import Model, ChatCompletionParamsNonStreaming, ChatCompletion

from openai.utils.client import openai_client
from openai.utils.cost import openai_cost, TokensCount, Price
from dataclasses import dataclass

@dataclass
class OpenAIChatInput:
    user_content: str
    system_content: str | None = None
    model: Model | None = None
    json_schema: dict = {
        "name": str,
        "description": str
    }
    price: Price | None = None
    api_key: str | None = None
    params: ChatCompletionParamsNonStreaming | None = None


async def openai_chat_completion_base(input: OpenAIChatInput) -> ChatCompletion:
    client = openai_client(input.api_key)