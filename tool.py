from openai import OpenAI
import os, sys, time
import pandas as pd

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(model=model, messages=messages, temperature=0)
    return response.choices[0].message.content


file = open(sys.argv[1], 'r')
Lines = file.readlines()

prompt = """
The lines follow this convention: The asterisk symbol (*) marks a main point.
The o character (o) marks a subpoint that belongs to the main point above it.
Given the following lines, generate 10 to 15 questions about the content of the lines.\n      
         """ 

count = 0
for line in Lines:
    count += 1
    prompt += line

print(get_completion(prompt))

file.close()