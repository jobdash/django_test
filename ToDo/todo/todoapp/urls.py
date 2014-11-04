from django.conf.urls import patterns, url

from todoapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)