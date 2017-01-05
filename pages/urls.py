# coding=utf-8
from django.conf.urls import url

from pages.views import DocumentDetailView, RegulationsListView, RegulationsDetailView, AllCategoryRegulationsListView

urlpatterns = [
    url(r'^normativnye_dokumenty/$', AllCategoryRegulationsListView.as_view(), name='AllCategoryRegulationsListView'),
    url(r'^normativnye_dokumenty/(?P<category>[a-zA-Z_\-0-9]*)/$', RegulationsListView.as_view(), name='RegulationsListView'),
    url(r'^normativnye_dokumenty/(?P<category>[a-zA-Z_\-0-9]*)/(?P<slug>[a-zA-Z_\-0-9]*)/$', RegulationsDetailView.as_view(), name='RegulationsDetailView'),
]
