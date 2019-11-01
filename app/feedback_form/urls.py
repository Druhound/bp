from django.conf.urls import url

from app.feedback_form.views import CallbackCreateView
from . import views
urlpatterns = [
    url(r'^ajax1/$', CallbackCreateView.as_view(), name='feedback'),
    # url(r'^ajax2/(?P<url>.*)$', FeedbackCreateView.as_view(), name='feedback'),
    url(r'^ajax2/$', views.send_email, name='feed'),
]