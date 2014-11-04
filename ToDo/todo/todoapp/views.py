from django.shortcuts import render
from django.http import HttpResponse
from models import Task

# creating the view

def index(request):
    return HttpResponse('Hello JobDash, you are at Kelsey Jacobsen\'s ToDo app')

def index(request):
    # lists of tasks
    tasks = Task.objects.all()
    # loads the index.html template
    context = {'tasks': tasks}
    return render(request, 'todoapp/index.html', context)
