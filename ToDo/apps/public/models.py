from django.db import models
from django import forms


class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task_complete = models.BooleanField(default=False)

    def __unicode__(self):
        return self.task_name



class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['task_name']