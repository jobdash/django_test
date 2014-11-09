from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from apps.public.models import Task, TaskForm


def task_list(request):

    list_of_tasks = Task.objects.filter(task_complete=False)
    template = loader.get_template('public/index.html')
    context = RequestContext(request, {
        'list_of_tasks': list_of_tasks,
    })
    return HttpResponse(template.render(context))

def get_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task_name = form.cleaned_data['task_name']
            form.save()
            return HttpResponseRedirect('/task_list')
        else:
            return HttpResponse("Not a valid task name. <a href='/task_list'>Click Here to try again</a>")

    else:  # creates a blank form if receiving a non-POST request
        form = TaskForm()

    return render(request, 'index.html', {'form': form})