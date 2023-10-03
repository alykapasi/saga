from django.shortcuts import redirect, render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import CreateNewStory
from .models import Story, UserPrompts, AiResponses
import openai

# Create your views here.
def home(request):
    return render(request, 'main/home.html', {})

def contact(request):
    return render(request, 'main/contact.html', {})

def profile(request):
    return render(request, 'main/profile.html', {})

def applet(request):
    return render(request, 'main/applet.html', {})

def todo(request):
    return render(request, 'main/todo.html', {})

@login_required
def saves(request):
    return render(request, 'main/saves.html', {})

@login_required
def new(request):
    if request.method == 'POST':
        form = CreateNewStory(request.POST)
        if form.is_valid():
            n = form.cleaned_data['story_id']
            s = Story(story_id=n, user=request.user)
            s.save()
        # fix redirect to story
        return HttpResponseRedirect('/saves')
    else:
        form = CreateNewStory()

    return render(request, 'main/new.html', {'form': form})

def xtra(request, id):
    story = Story.objects.get(story_id=id)
    
    if request.method == 'POST':
        prompt_text = request.POST.get('prompt')
        user_prompt = UserPrompts.objects.create(story=story, prompt=prompt_text)
        response = get_ai_response(prompt_text)
        AiResponses.objects.create(prompt=user_prompt, response=response)
    
    # Retrieve the latest UserPrompts object for the current story if it exists
    try:
        user_prompt = UserPrompts.objects.filter(story=story).latest('id')
        ai_responses = AiResponses.objects.filter(prompt=user_prompt)
        chatlog = zip([user_prompt], ai_responses)
    except UserPrompts.DoesNotExist:
        chatlog = []
    
    return render(request, 'main/xtra.html', {'story': story, 'chatlog': chatlog})

def get_ai_response(prompt):
    openai.api_key = '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'
    response = openai.ChatCompletion.create(
        engine='gpt-3.5-turbo-16k',
        prompt=prompt,
        max_tokens=300,
        temperature=0.75,
    )
    if 'choices' in response and len(response.choices) > 0:
        return response.choices[0].text.strip()
    else:
        return ''


