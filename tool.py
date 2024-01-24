from openai import OpenAI
import os, sys, time
import pandas as pd

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(model=model, messages=messages, temperature=0)
    return response.choices[0].message.content


file = open('file.txt', 'r')
Lines = file.readlines()

count = 0
for line in Lines:
    count += 1
    print(get_completion(line.strip()))

file.close()
