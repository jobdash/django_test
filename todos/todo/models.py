from django.db import models
from django.contrib.auth.models import User


# models here.
importance_choices = (
    ('A', 'Very Important'),
    ('B', 'Important'),
    ('C', 'Medium'),
    ('D', 'Unimportant'),
)

status_choices = (
    ('A', 'In Progress'),
    ('B', 'Completed'),
    ('C', 'On Hold'),
)


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    importance = models.CharField(
        max_length=1,
        choices=importance_choices
    )

    status = models.CharField(
        max_length=1,
        choices=status_choices
    )

    owner = models.ForeignKey(User)

    def text_status(self):
        return dict(status_choices)[self.status]

    def text_importance(self):
        return dict(importance_choices)[self.importance]

    def short_description(self):
        return self.description.split('\n')[0][:80]

    def __unicode__(self):
        return self.title