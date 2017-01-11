# coding=utf-8
from django.http import HttpResponse
from django.conf import settings
from django.views.generic import CreateView
from django.core.mail import send_mail
from django.utils.translation import ugettext as _

import json

from .forms import OrderServiceForm, CallbackForm, CallbackSOUTForm, CallbackExpertsForm


class FeedbackCreateView(CreateView):
    model = CallbackForm
    form_class = CallbackForm
    template_name = 'Callback_emailform.html'

    # Походу получаем данные из форм
    def get_form_kwargs(self):
        kwargs = super(FeedbackCreateView, self).get_form_kwargs()
        return kwargs

    # Костыльный (пока что) метод отправки письма
    def form_valid(self, form):
        response = super(FeedbackCreateView, self).form_valid(form)
        if hasattr(settings, 'FEEDBACK_EMAIL'):
            d = form.cleaned_data
            try:
                send_mail('Тело письма',
                          'email: Имя:{} Комментарий:{} Телефон:{}'.format(d['name'], d['text'], d['telephone']),
                          settings.SERVER_EMAIL, [settings.FEEDBACK_EMAIL]
                        )
            except:
                return HttpResponse(json.dumps({'error': _('Failed to send email')}))
        return HttpResponse(json.dumps({}))

    def form_invalid(self, form):
        return HttpResponse(json.dumps({'errors': form.errors}))

    # url, на который мы переходим после отправки
    def get_success_url(self):
        return self.kwargs['url']

# class OrderServiceForm(FormView):
#
