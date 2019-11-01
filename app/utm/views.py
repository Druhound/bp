from django.views.generic import TemplateView
from app.utm.models import Utm


class TemplateView2(TemplateView):
    template_name = "template.html"
    utm = None

    def get(self, request, *args, **kwargs):
        try:
            utm_id = self.request.GET['utm_campaign']
        except:
            utm_id = None
        if utm_id:
            self.utm = Utm.objects.get(name=utm_id)
        else:
            self.utm = ""
        return super(TemplateView2, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TemplateView2, self).get_context_data(**kwargs)
        context['utm'] = self.utm
        return context

    # ?utm_source = yandex & utm_medium = cpc & utm_campaign = content_8