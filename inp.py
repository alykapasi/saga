## this is the script that will start as the opening
## determine whether the user wants to modify or create a story
import os
import openai

def determine_mode():
    while True:
        mode = input("Please enter:\n\
                     1) If you would like to generate a new story line\n\
                     2) If you would like to modify an existing story line\n\
                     3) If you would like to resume a previous story\n")
        
        if mode in ["1", "2", "3"]:
            break
        
        print("ERROR: Incorrect value, please enter a number betwen 1 and 3.\n")

    match int(mode):
        case 1:
            print("Ok! Let's spin a new tale!\n")
            return 1
        case 2:
            print("Awesome! Let's modify a story!\n")
            return 2
        case 3:
            print("Sure! Let's continue where we left off!\n")
            ## check if a story is saved...
            ## create a .json file to store the saved story -> if empty that means no saved story
            return 3
        case _:
            print("ERROR!!!!!!")
            return 0
        
def create_story():
    logs = []
    pass


def modify_story():
    story_name = story_loc = None
    while True:
        story = input("What story would you like to modify?:\n")
        ## check if the story exists with the openai api
        ## if yes the break, else prompt for a known story
        msg1 = {'role': 'user', 'content': f'if you know about a story titled: {story} then return 1, else return 0'}
        verify1 = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=msg1,
            temperature=0,
            max_tokens=1,
            )
        if verify1.choices[0].message['content'] == '1':
            story_name = story
            break
        else:
            print("Sorry, I don't know it, please try again.")
    
    while True:
        loc = input("What part of the story would you like to modify?:\n ")
        msg2 = {'role': 'user', 'content': f'is {loc} in the {story_name}? if yes then return 1, else return 0'}
        verify2 = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=msg1,
            temperature=0,
            max_tokens=1,
            )
        if verify2.choices[0].message['content'] == '1':
            story_loc = loc
            break
        else:
            print("Sorry, I don't think that happens in the story, please input a different point.\n")


def continue_story():
    pass

if __name__ == "__main__":
    ## get the api key from the .env file
    openai.api_key = os.getenv('OPENAI_API_KEY')
    mode = determine_mode()
    match mode:
        case 1:
            create_story()
        case 2:
            modify_story()
        case 3:
            continue_story()