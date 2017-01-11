from django.conf.urls import url

from app.feedback_form.views import FeedbackCreateView

urlpatterns = [
    url(r'^ajax/(?P<url>.*)$', FeedbackCreateView.as_view(), name='feedback'),
]