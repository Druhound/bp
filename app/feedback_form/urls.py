from django.conf.urls import url

from app.feedback_form.views import FeedbackCreateView, CallbackCreateView
from . import views
urlpatterns = [
    url(r'^ajax1/(?P<url>.*)$', CallbackCreateView.as_view(), name='feedback'),
    url(r'^ajax2/(?P<url>.*)$', FeedbackCreateView.as_view(), name='feedback'),
    url(r'^2ajax/$', views.send_email, name='feed'),
]