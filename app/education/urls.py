# coding=utf-8
from django.conf.urls import url

from app.education import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<slug>.*)$', views.education_view, name='page'),
    # url(r'^(?P<slug>.*)$', views.education_view, name='page'),
]