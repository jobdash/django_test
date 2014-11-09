from django.conf.urls import patterns, url
from apps.public import views


urlpatterns = patterns('',
	#ex: /task_list/
    url(r'^$', views.task_list, name='task_list'),
    # url(r'^$', views.get_task, name='get_task'),
    #ex: /task_list/5
    url(r'^get_task/', views.get_task, name='get_task'),
    # url(r'^(?P<task_id>\d+)/$', views.get_task, name='get_task'),
)