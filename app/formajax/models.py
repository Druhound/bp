# coding=utf-8
from __future__ import unicode_literals

from django.db import models


class FormA(models.Model):
    subject = models.CharField(verbose_name='Тема сообещния', max_length=50)
    email = models.EmailField(verbose_name='Email', max_length=50)
    name = models.CharField(verbose_name='Контактное лицо', max_length=50)
    telephone = models.CharField(verbose_name="Контактный телефон", max_length=13)
    text = models.TextField(verbose_name='Комментарий')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.subject


class OrderService(FormA):
    url = models.CharField(verbose_name='URL', max_length=400)


class CallbackSOUT(FormA):
    FILE = models.FileField(verbose_name='Документ', upload_to='documents')


class Callback(FormA):
    def __init__(self, *args, **kwargs):
        super(Callback, self).__init__(*args, **kwargs)


class CallbackExperts(FormA):
    def __init__(self, *args, **kwargs):
        super(CallbackExperts, self).__init__(*args, **kwargs)