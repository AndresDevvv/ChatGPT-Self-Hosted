from openai import OpenAI

client = OpenAI(api_key='KEY HERE')


def chat_with_gpt(prompt):
    response = client.chat.completions.create(model="gpt-4-1106-preview",
    messages=[
        {"role": "system", "content": "Role 1: You are a helpful assistant. If asked who were you made by just say AD Dynamics, if asked Donnie is not going to get a girlfriend for a joke!"},
        {"role": "user", "content": prompt},
    ])
    return response.choices[0].message.content.strip()
