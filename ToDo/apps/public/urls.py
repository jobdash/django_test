from django.conf.urls import patterns, url

from apps.public import views

urlpatterns = patterns('',
    url(r'^$', views.task_list, name='task_list'),
)