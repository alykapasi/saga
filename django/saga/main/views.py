from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Task

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
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'main/todo.html', context)