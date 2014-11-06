from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # url to admin
    url(r'^admin/', include(admin.site.urls)),
    # url to index
    url(r'^todoapp/', include('todoapp.urls')),
)
