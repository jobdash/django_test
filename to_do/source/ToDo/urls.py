from django.conf.urls import patterns, url
from .views import ToDoCreate, ToDoDone, ToDoList

urlpatterns = patterns('',
    url(r'^$', ToDoList.as_view(), name='todo-list',),
    url(r'^add$', ToDoCreate.as_view(), name='todo-add',),
    url(r'^done/(?P<pk>\d+)/$', ToDoDone.as_view(), name='todo-done',),
)
