from openai import OpenAI

client = OpenAI(
    api_key="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"
)

response = client.responses.create(
    model="gpt-4o-mini",
    input="write a haiku about ai",
    store=True,
)

print(response.output_text)
