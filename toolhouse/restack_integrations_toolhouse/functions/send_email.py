from pydantic import BaseModel
from restack_ai.function import function
from openai import OpenAI
from restack_integrations_toolhouse.utils.toolhouse_client import toolhouse_client

class MailInput(BaseModel):
    subject: str
    body: str
    to: str
    openai_api_key: str | None = None
    toolhouse_api_key: str | None = None


@function.defn(name="mail_website_summary")
async def mail_website_summary(input: MailInput) -> str:
    client = OpenAI(api_key=input.openai_api_key)
    th = toolhouse_client(api_key=input.toolhouse_api_key, provider="openai")

    messages = [
        {"role": "user", "content": f"Send email to {input.to} with the following subject: {input.subject} and body: {input.body}"},
    ]   

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=th.get_tools()
    )

    messages += th.run_tools(response, append=True)

    print(messages)

    client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=th.get_tools()
    )

    return "Email sent successfully"
