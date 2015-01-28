"""
    Models for the ToDo app.
"""
from django.db import models
from django.core.urlresolvers import reverse


class ToDo(models.Model):
    """ Main Model. """
    created = models.DateField(auto_now_add=True, editable=False)
    todo = models.TextField()
    compleated = models.DateField(editable=False, null=True)

    def get_absolute_url(self):
        """ what is my name again? """
        return reverse('todo:todo-list')
