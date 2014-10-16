from django.conf.urls import patterns
from django.contrib import admin
admin.autodiscover()
import todo.views


urlpatterns = patterns('',
    (r'^login$', todo.views.todo_login),
    (r'^logout$', todo.views.todo_logout),

    (r'^$', todo.views.todo_index),
    (r'^add$', todo.views.add_todo),
    (r'^delete/(?P<todo_id>\d+)', todo.views.delete_todo),
    (r'^update/(?P<todo_id>\d+)', todo.views.update_page),
    (r'^save/(?P<todo_id>\d+)', todo.views.update_todo),
)