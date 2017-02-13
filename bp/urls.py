# coding=utf-8
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url
from django.contrib import admin
from views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^search/', include('haystack.urls', namespace='search')),
    url(r'^normativnye_dokumenty/', include('app.pages.urls', namespace='pages')),
    url(r'^feedback/', include('app.feedback_form.urls', namespace='form')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()