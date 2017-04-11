# coding=utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.DocumentDetailView.as_view()),
    # url(r'^$', views.AllCategoryRegulationsListView.as_view(), name='index'),
    # url(r'^(?P<category>[^/]*)/$', views.RegulationsListView.as_view(), name='list'),
    # url(r'^(?P<category>[^/]*)/(?P<slug>[^/]*)/$', views.RegulationsDetailView.as_view(), name='detail')
]
