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
            form.save()
            return HttpResponseRedirect('/task_list')

        else:  # mostly to prevent blank responses, but will prevent other problematic inputs if they exist
            return HttpResponse("Not a valid task name. <a href='/task_list'>Click Here to try again</a>")

    else:  # creates a blank form if receiving a non-POST request
        form = TaskForm()

    return HttpResponseRedirect("/task_list")


def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.task_complete = True
    task.save()
    return HttpResponseRedirect('/task_list')