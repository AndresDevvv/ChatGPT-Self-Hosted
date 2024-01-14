from openai import OpenAI

client = OpenAI(api_key='PUT YOUR KEY HERE')


def chat_with_gpt(prompt):
    response = client.chat.completions.create(model="babbage-002",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ])
    return response.choices[0].message.content.strip()
