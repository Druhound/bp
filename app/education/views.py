from __future__ import print_function

from django.shortcuts import render
from django.http import Http404, HttpResponsePermanentRedirect
from django.views.generic import TemplateView

from app.education.models import Education, Locations


class IndexView(TemplateView):
    template_name = 'education/Education-templates/Education-index.html'
    context_object_name = 'education_list'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['locations'] = Locations.get_published.all()
        return context


def education_view(request, slug):
    context = {}
    # print(slug)
    # if not slug.endswith('/'):
    #     slug += '/'
    # print(slug)
    try:
        page = Education.get_published.get(slug=slug)
    except:
        if not slug.endswith('/'):
            return HttpResponsePermanentRedirect('%s/' % request.path)
        else:
            raise Http404
    template = 'education/Education-templates/Education' + page.templates + '.html'
    context['education'] = page
    return render(request, template, context)
