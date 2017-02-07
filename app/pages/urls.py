# coding=utf-8
from django.conf.urls import url

from app.pages.views import RegulationsListView, RegulationsDetailView, AllCategoryRegulationsListView

urlpatterns = [
    url(r'^$', AllCategoryRegulationsListView.as_view(), name='index'),
    url(r'^(?P<category>[^/]*)/$', RegulationsListView.as_view(), name='list'),
    url(r'^(?P<category>[^/]*)/(?P<slug>[^/]*)/$', RegulationsDetailView.as_view(), name='detail'),
    #url(r'^list$', views.product_list)
]
