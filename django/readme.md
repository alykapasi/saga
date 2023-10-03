# Shakespeare.ai

## Aly Kapasi

### Idea

I am an avid gamer, and enjoyer of stories and media. A big issue I have is I get too drawn into the story, usually to the point of obsession. I commonly think this character is so stupid, if I was in their place I would do this differently.
Now that powerful AI agents like ChatGPT4 and Midjourney are openly accessible, I felt like there is something that I can do.

My idea is to leverage these AI agents to create a story that I can control and guide to my liking. Ideally, the AI henceforth referred to as Shakespeare will be able to do just that. Shakespeare will be able to generate completely new stories all on its own or modify existing stories from a specified point by the user. Shakespeare should also be able to take in user input as a prompt: if empty decide by itself or if a prompt is entered then it should generate according to what the user wants.

### Implentation Checklist

#### 1

Create a front-end for the OPENAI API, so that I can interact with Shakespeare thru a webpage

#### 2

Specialize the model to only work on story generation and modification

#### 3

Make sure only the relevant inputs are accepted and all other inputs are flushed and not used

#### 4

Create a backend to store all the queries so backtracking is possible (use PineCone) and essentially create a full decision tree for each fork

#### 5

Create a specialized LLM that is trained only on works of fiction -> (novels, short stories, web stories, fan fics, comics, cartoons, graphic novels, manga, etc.)

#### 6

Create a proper UI for the website and start developing an application

#### 7

CI/CD -> minor fixes and alterations as needed
