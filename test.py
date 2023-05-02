import os
import openai

openai.api_key = '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'

# First determine whether the user wants to modify a story
# or create on from scratch
starting_message = [{'role': 'user', 'content': 'If you know about a story titled: \'Humpty Dumpty\' return 1, else return 0!'}]

completion = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=starting_message,
    temperature=0,
    max_tokens=100,
    presence_penalty=0,
    frequency_penalty=0,
)

print(completion.choices[0].message['content'])