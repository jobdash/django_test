from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from apps.public.models import Task

def task_list(request):
	list_of_tasks = Task.objects.filter(task_complete=False)
	template = loader.get_template('public/index.html')
	context = RequestContext(request, {
		'list_of_tasks': list_of_tasks,
	})
	
	# output = "\n".join(p.task_name for p in list_of_tasks)
	return HttpResponse(template.render(context))
