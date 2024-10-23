from pydantic import BaseModel
from restack_ai.function import function
from openai import OpenAI
from restack_integrations_toolhouse.utils.toolhouse_client import toolhouse_client

class WebsiteInput(BaseModel):
    url: str
    openai_api_key: str | None = None
    toolhouse_api_key: str | None = None


@function.defn(name="summarize_website")
async def summarize_website(input: WebsiteInput) -> str:
    client = OpenAI(api_key=input.openai_api_key)
    th = toolhouse_client(api_key=input.toolhouse_api_key, provider="openai")

    messages = [
        {"role": "user", "content": f"Get the contents of {input.url} and summarize its key value propositions in three bullet points."},
    ]    

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=th.get_tools()
    )

    messages += th.run_tools(response, append=True)

    print(messages)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=th.get_tools()
    )

    return response.choices[0].message.content
