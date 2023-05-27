## main
import openai
from src import *

openai.api_key = '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'

if __name__ == '__main__':
    n = choose_story()
    # in beta version force the user to be narrator expand later
    role =  1
    story_name = choice_list[n-1]
    user_role = role_list[role-1]

    prompt = f'You will be a story-telling/modifying AI\
        the story will be {story_name} and the user will assume {user_role}\
        role. I want you to give a brief outline of the main points\
        in the story in a list format, so the user can choose where\
        they want to start the story. The user will be prompted for\
        decisions at crucial points in the story, and you will alter\
        the story based on the decisions. The user will be able to\
        change the story based on their own ideas. Only return a list\
        with the major points in the story the list should be exactly\
        10 points long.'

    prompts = [{'role':'user', 'content':prompt}]
    print(f'You are a {user_role} in {story_name}.')
    
    homer = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = prompts,
        temperature = 0.0,
        max_tokens = 360,
    )
    output = homer.choices[0].message['content']
    print(output)
    prompts.append({'role':'assistant', 'content':output})

    while True:
        try:
            entry_point = int(input('Enter the number of the point in the story you would like to start at: '))
            if entry_point in range(1,11):
                break
            else:
                print('Invalid entry, try again.')
        except:
            print('Invalid entry, try again.')

    prompt = f'You will start at point {entry_point}, provide a detailed description of the point in the story.\
        Try to stay as close to the written part of the story as possible, the ideal response should be about a\
        a paragraph long. Then prompt the user as to what decision they should take, leave it open-ended,\
        but provide guidance as to what directions they can take.'

    prompts.append({'role':'user', 'content':prompt})
        
    homer = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = prompts,
        temperature = 0.0,
        max_tokens = 360,
    )
    output = homer.choices[0].message['content']
    prompts.append({'role':'assistant', 'content':output})
    print('\n' + output)

    while True:
        user_prompt = input('> ')
        if user_prompt == '\\!q':
            print('\nThe End.\nGoodbye!')
            break
        else:
            prompts.append({'role':'user', 'content':user_prompt})
            homer = openai.ChatCompletion.create(
                model = 'gpt-3.5-turbo',
                messages = prompts,
                temperature = 1.0,
                max_tokens = 500,
            )
            output = homer.choices[0].message['content']
            prompts.append({'role':'assistant', 'content':output})
            print('\n' + output)

    print('Thank You for your using Homer.ai')