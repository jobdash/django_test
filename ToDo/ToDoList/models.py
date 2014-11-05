from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task_complete = models.BooleanField(default=False)

    def __unicode__(self):
        return self.task_name

    def is_complete(self):
        return self.task_complete