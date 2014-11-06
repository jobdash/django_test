from django.db import models
from django import forms

# Create your models here.
# Task model - text input for a ToDo item
class Task(models.Model):
    task_text = models.CharField(max_length=75)         #input for the task
    task_status = models.BooleanField(default=False)    #mark as done / default incomplete
    task_input = forms.CharField(label='task to do')
    
    def __str__(self):
        return self.task_text

# Submit new task
class TaskForm(forms.Form):
    task_submit = forms.CharField(label='new task', max_length=75)

    def __str__(self)
        return self.task_submit