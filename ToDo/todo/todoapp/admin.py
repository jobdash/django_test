from django.contrib import admin
from todoapp.models import Task

class TaskAdmin(admin.ModelAdmin):
    fields = ['task_text', 'task_status']
    list_display = ('task_text', 'task_status')

# registering models
admin.site.register(Task)