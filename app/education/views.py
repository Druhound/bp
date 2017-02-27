from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView

from app.education.models import Education


class IndexView(TemplateView):
    template_name = 'education/Education-templates/Education-index.html'
    context_object_name = 'education_list'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


def education_view(request, slug):
    context = {}
    try:
        page = Education.get_published.get(slug=slug)
    except:
        raise Http404
    template = 'education/Education-templates/Education' + page.templates + '.html'
    context['education'] = page
    return render(request, template, context)
