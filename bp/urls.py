# coding=utf-8
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search/', include('haystack.urls')),
    url(r'^normativnye_dokumenty/', include('pages.urls', namespace='pages')),
]
