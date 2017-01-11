# coding=utf-8
from django.conf.urls import include, url
from django.contrib import admin
from views import IndexView
from ajax import views

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^search/', include('haystack.urls')),
    url(r'^normativnye_dokumenty/', include('app.pages.urls', namespace='pages')),
    url(r'^fb2/', include('app.feedback_form.urls')),
]
