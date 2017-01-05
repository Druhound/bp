# coding=utf-8
from django.conf.urls import url

from search.views import PlaceListView, Index


urlpatterns = [
    url(r'^$', Index.as_view(), name='search'),
    url(r'^result', PlaceListView.as_view(), name='result'),
]