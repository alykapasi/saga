import os
import openai

openai.api_key = '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'

# First determine whether the user wants to modify a story
# or create on from scratch
starting_message = [{'role': 'user', 'content': 'Hello!'}]

completion = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=starting_message,
    temperature=0,
    max_tokens=100,
    presence_penalty=0,
    frequency_penalty=0,
)

print(completion.choices[0].message['content'])