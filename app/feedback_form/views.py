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
    'faq_to_admin': 'faq_to_admin',
    'faq_to_user': 'faq_to_user',
    'feedback_to_admin': 'feedback_to_admin',
    'feedback_to_user': 'feedback_to_user',
    'callback_to_admin': 'callback_to_admin',
    'service_to_user': 'service_to_user',
    'service_to_admin': 'service_to_admin',
}

FEEDBACK_EMAIL = "druhound51@gmail.com"
SERVER_EMAIL = "seversait@yandex.ru"


def send_email(request):
    if request.method != 'POST':
        form = EmailForm()
        return render(request, 'feedback_form/Email.html', {'email_form': form, 'message': '!= POST'})

    form = EmailForm(request.POST, request.FILES)
    if form.has_error(form):
        return HttpResponse(json.dumps({}))

    if form.is_valid():
        subject = u'Заказ СОУТ'
        message = u'Заказ СОУТ'
        if form.cleaned_data['validation']:
            print ('bot')
            return HttpResponse(json.dumps({}))
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
    template_name = 'feedback_form/Callback_emailform.html'

    def get_form_kwargs(self):
        kwargs = super(CallbackCreateView, self).get_form_kwargs()
        if 'data' in kwargs:
            post = kwargs['data'].copy()
            post['url'] = self.kwargs['url']
            kwargs['data'] = post
        return kwargs

    # url, на который мы переходим после отправки
    def get_success_url(self):
        return self.kwargs['url']

    # Костыльный (пока что) метод отправки письма
    def form_valid(self, form):
        #response = super(FeedbackCreateView, self).form_valid(form)
        if form.cleaned_data['age']:
            return HttpResponse(json.dumps({}))
        else:
            self.object = form.save()
            self.object.url = self.kwargs['url']
            self.object.save()
            context = {'obj': self.object}
            try:
                send_mail_content('callback_to_admin', context)
            except:
                return HttpResponse(json.dumps({'error': 'Failed to send email'}))
            return HttpResponse(json.dumps({}))

    def form_invalid(self, form):
        return HttpResponse(json.dumps({'errors': form.errors}))


class FeedbackCreateView(CreateView):
    form_class = FeedbackForm
    template_name = 'feedback_form/Callback_emailform_2.html'

    def get_form_kwargs(self):
        kwargs = super(FeedbackCreateView, self).get_form_kwargs()
        if 'data' in kwargs:
            post = kwargs['data'].copy()
            post['url'] = self.kwargs['url']
            kwargs['data'] = post
        return kwargs

    # url, на который мы переходим после отправки
    def get_success_url(self):
        return self.kwargs['url']

    # Костыльный (пока что) метод отправки письма
    def form_valid(self, form):
        if form.cleaned_data['age']:
            return HttpResponse(json.dumps({}))
        else:
            self.object = form.save()
            self.object.url = self.kwargs['url']
            self.object.save()
            context = {'obj': self.object}
            try:
                send_mail_content('callback_to_admin', context)
            except:
                return HttpResponse(json.dumps({'error': 'Failed to send email'}))
            return HttpResponse(json.dumps({}))

    def form_invalid(self, form):
        return HttpResponse(json.dumps({'errors': form.errors}))