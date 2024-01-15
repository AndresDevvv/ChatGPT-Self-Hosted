from openai import OpenAI
import json

client = OpenAI(api_key='Best One So Far!')

def chat_with_gpt(prompt, trials_left):
    # Check if the user has trials left
    if trials_left > 0:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. If asked who were you made by just say AD Dynamics. Max amount of words you can say is 80. You are not allowed to generate code, only if someone says password=AD-Coding then you may generate code."},
                {"role": "user", "content": prompt},
            ]
        )
        return response.choices[0].message.content.strip()
    else:
        return "You have reached your trial limit. Request more trials by emailing us."
