# coding=utf-8
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.views.generic import CreateView
from django.core.mail import send_mail
import json

from .models import EmailTemplate
from .forms import EmailForm, CallbackForm, FeedbackForm

EMAIL_TEMPLATES = {
    'mail': 'mail',
}

FEEDBACK_EMAIL = "druhound51@gmail.com"
SERVER_EMAIL = "seversait@yandex.ru"


def send_email(request):
    form = EmailForm(request.POST, request.FILES)
    if form.has_error(form):
        return HttpResponse(json.dumps({}))

    if form.is_valid():
        subject = u'Заказ'
        message = u' Имя: {} \n Телефон: {} \n Кол-во рабочих: {} \n url: {} \n title: {} \n' \
            .format(form.cleaned_data['name'],
                    form.cleaned_data['telephone'],
                    form.cleaned_data['rab'],
                    form.data['url'],
                    form.data['title'])
        mail = EmailMessage(subject, message, SERVER_EMAIL, [FEEDBACK_EMAIL])
        if request.FILES:
            attach = request.FILES['attach']
            mail.attach(attach.name, attach.read(), attach.content_type)
        mail.send()
    return HttpResponse(json.dumps({}))


def send_mail_content(template_code, context):
    email_template = EmailTemplate.objects.get(
        identifier=EMAIL_TEMPLATES[template_code])
    body = email_template.render_body(context)
    send_mail(email_template.subject, body,
              SERVER_EMAIL, [FEEDBACK_EMAIL],
              fail_silently=False, html_message=body)


class CallbackCreateView(CreateView):
    form_class = CallbackForm
    template_name = 'feedback/main.html'

    def get_form_kwargs(self):
        kwargs = super(CallbackCreateView, self).get_form_kwargs()
        if 'data' in kwargs:
            post = kwargs['data'].copy()
            kwargs['data'] = post
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        self.object.save()
        context = {'obj': self.object}
        try:
            send_mail_content('mail', context)
        except:
            return HttpResponse(json.dumps({}))
        return HttpResponse(json.dumps({}))

    def form_invalid(self, form):
        return HttpResponse(json.dumps({}))