# coding=utf-8
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url
from django.contrib import admin
from views import IndexView
from app.utm.views import TemplateView2
from app.graphics import views



urlpatterns = [
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
    # url(r'^grap/', views.view_func),
    url(r'^utm/$', TemplateView2.as_view(), name='utm'),
    # url(r'^search/', include('haystack.urls', namespace='search')),
    # # url(r'^normativnye_dokumenty/', include('app.pages.urls', namespace='pages')),
    # url(r'^educations/', include('app.education.urls', namespace='education')),
    # url(r'^feedback/', include('app.feedback_form.urls', namespace='form')),
    # url(r'^(?P<slug>.*)$', include('app.pages.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()