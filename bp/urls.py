# coding=utf-8
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url
from django.contrib import admin
from views import IndexView
from app.pages import views

urlpatterns = [
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^search/', include('haystack.urls', namespace='search')),
    url(r'^normativnye_dokumenty/', include('app.pages.urls', namespace='pages')),
    url(r'^educations/', include('app.education.urls', namespace='education')),
    url(r'^feedback/', include('app.feedback_form.urls', namespace='form')),
    url(r'^(?P<slug>.*/)$', views.DocumentDetailView.as_view(), name='list_2'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()