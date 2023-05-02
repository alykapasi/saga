import os
import openai
from src import *

if __name__ == '__main__':
    openai.api_key = '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'
    print(choices)

    while True:
        choice = input('Which story would you like to choose?: ')
        try:
            choice = int(choice)
            if 1 <= choice <= 23:
                break
            else:
                print('Please input a number between 1-23...\n')
        except:
            print('Please input a number between 1-23...\n')

    chosen = choice_list[choice-1]

    ## initial prompt: guide the AI to be better suited to the task and choose a story and return a brief synopsis
    guide = 'I want you to be a story telling AI, and modify the story of {}\
            to my liking. Firstly, give me a brief summary of the story'\
            .format(chosen)
    
    prompts = [{'role':'user', 'content': guide}]
    gpt = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = prompts,
        temperature = 0.0,
    )

    ## print the response
    print(gpt.choices[0].message['content'])
    prompts.append({'role':'ai', 'content':gpt.choices[0].message['content']})

    ## second prompt: choose the role user wants to play
    while True:
        choice = input('Please choose your role:\n\ 1. Narrator\n\ 2. Character\n')
        try:
            if choice == '1':
                role = 'narrator'
                break
            elif choice == '2':
                role = 'character'
                ch = input('What character would you like to be?: ')
                break
            else:
                print('invalid choice...\n')
        except:
            print('invalid choice...\n')

    ## third prompt: choose where they wish to continue the story from
    locn = input('Where in the story would you like to start from?: ')

    guide_followup_ch = 'I will assume the role of a character named: '.format()

    prompts.append({'role':'user', 'content':''})

    gpt = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = prompts,
        temperature = 0.0,
    )