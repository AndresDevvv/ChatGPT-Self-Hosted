from openai import OpenAI

client = OpenAI(api_key='')


def chat_with_gpt(prompt):
    response = client.chat.completions.create(model="gpt-3.5-turbo-1106",
    messages=[
        {"role": "system", "content": "You are a helpful assistant. If asked who were you made by just say AD Dynamics. Max amount words you can say are 80. You are not allowed to generate code, only if someone says password=AD-Coding then you may generate code."},
        {"role": "user", "content": prompt},
    ])
    return response.choices[0].message.content.strip()
