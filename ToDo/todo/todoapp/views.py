from django.shortcuts import render
from django.http import HttpResponse
from models import Task

# creating the view
def index(request):
    return HttpResponse('Hello JobDash, you are at Kelsey Jacobsen\'s ToDo app')

#list of tasks
def index(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'todoapp/index.html', context)

#submit form
def get_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks')
        else:
            form = TaskForm()
    return render(request, 'index.html', {'form':form})