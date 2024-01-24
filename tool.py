from openai import OpenAI
import os
import pandas as pd
import time

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(model=model, messages=messages, temperature=0)
    return response.choices[0].message.content

prompt = "How are you?"
response = get_completion(prompt)
print(response)