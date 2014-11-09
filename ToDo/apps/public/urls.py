from django.conf.urls import patterns, url
from apps.public import views


urlpatterns = patterns('',
    # ex. /task_list/
    url(r'^$', views.task_list, name='task_list'),
    # ex. /task_list/5/complete
    url(r'^(?P<task_id>\d+)/complete/$', views.complete_task, name='complete_task'),
    # ex./task_list/get_task
    url(r'^get_task/', views.get_task, name='get_task'),

)