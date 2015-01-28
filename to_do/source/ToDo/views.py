"""
    Here are the ToDo views.
    I Chose to go with class based views as they are bit more difficult to
    build and manage.
"""
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import ToDo
from .forms import ToDoForm


class ToDoCreate(CreateView):
    """ Lets create a todo. """
    model = ToDo
    form_class = ToDoForm
    success_url = reverse_lazy('todo:todo-list')


class ToDoDone(UpdateView):
    """ Lets mark a todo as done. """
    model = ToDo
    fields = []
    success_url = reverse_lazy('todo:todo-list')

    def get(self, request, *args, **kwargs):
        """ Over rideing 'get' to mark the todo done from a get. """
        super(ToDoDone, self).get(request, *args, **kwargs)
        self.object = self.get_object()
        self.object.compleated = datetime.now()
        self.object.save()
        return HttpResponseRedirect(reverse('todo:todo-list'))


class ToDoList(ListView):
    """ Lets list it out baby! """
    template_name = 'ToDo/index.html'
    queryset = ToDo.objects.filter(compleated__isnull=True)
