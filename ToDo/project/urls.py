from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ToDo.views.home', name='home'),
    url(r'^task_list/', include('apps.public.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
