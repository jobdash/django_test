from django.conf.urls import patterns, url
from apps.public import views


urlpatterns = patterns('',
	#ex: /task_list/
    url(r'^$', views.task_list, name='task_list'),
    #ex: /task_list/5
    # url(r'^(?P<task_id>\d+)/$', views.detail, name='detail'),
)