from django.db import models

# Create your models here.
# Task model - text input for a ToDo item
class Task(models.Model):
    task_text = models.CharField(max_length=75)         #input for the task
    task_status = models.BooleanField(default=False)    #mark as done / default incomplete
    def __str__(self):
        return self.task_text

# list of unfinished todos