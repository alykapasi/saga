import os
import openai

openai.api_key = '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'

# Combine conversation history into a single string
messages = [{'role': 'user', 'content': 'Write a story about Humpty-Dumpty and the backstory to his fall in murder mystery format'}]

completion = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=messages,
    temperature=1.0,
    max_tokens=1000,
    presence_penalty=0.75,
    frequency_penalty=0.75,
)

print(completion.choices[0].message['content'])
