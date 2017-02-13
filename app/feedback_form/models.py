# coding=utf-8
from __future__ import unicode_literals
from django.template import Template, Context
from django.core.exceptions import ValidationError
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _


from django.db import models


class EmailTemplate(models.Model):
    identifier = models.CharField(max_length=100, verbose_name='Уникальный идентификатор')
    subject = models.CharField(max_length=100, verbose_name='Тема')
    admin_email = models.EmailField(max_length=254, verbose_name='E-mail администратора')
    body = models.TextField(verbose_name='Тело', help_text='Доступные переменные:')

    class Meta:
        verbose_name = u'Шаблон письма'
        verbose_name_plural = u'Шаблоны писем'

    def __unicode__(self):
        return self.identifier

    @staticmethod
    def render_email_part(content, context):
        mail_template = Template(content)
        mail_context = Context(context)
        return mail_template.render(mail_context)

    def render_body(self, context):
        return self.render_email_part(self.body, context)


class Callback(models.Model):
    name = models.CharField(verbose_name='Контактное лицо', max_length=50)
    telephone = models.CharField(verbose_name="Контактный телефон", max_length=17, blank=True)
    text = models.TextField(verbose_name='Комментарий', blank=True)
    title = models.CharField(verbose_name="Страница с формой", max_length=50, blank=True)
    url = models.CharField(max_length=255, verbose_name=_('url'), blank=True)
    age = models.CharField(verbose_name='Возраст', max_length=10, blank=True,
                           help_text='(Используется для фильтрации спама)')

    def __unicode__(self):
        return u'{url}: {name}'.format(url=self.url, name=self.name)


class Feedback(models.Model):
    title = models.CharField(verbose_name="Название формы", max_length=50)
    name = models.CharField(verbose_name='Контактное лицо', max_length=50)
    telephone = models.CharField(verbose_name="Контактный телефон", max_length=17, blank=True)
    text = models.TextField(verbose_name='Комментарий', blank=True)
    url = models.CharField(max_length=255, verbose_name=_('url'), blank=True)
    age = models.CharField(verbose_name='Возраст', max_length=10, blank=True,
                           help_text='(Используется для фильтрации спама)')

    def __unicode__(self):
        return u'{url}: {name}'.format(url=self.url, name=self.name)


class CallbackSOUT2(models.Model):
    subject = models.CharField(verbose_name='Тема сообещния', max_length=50)
    email = models.EmailField(verbose_name='Email', max_length=50)
    name = models.CharField(verbose_name='Контактное лицо', max_length=50)
    telephone = models.CharField(verbose_name="Контактный телефон", max_length=17)
    text = models.TextField(verbose_name='Комментарий')
    document = models.FileField(verbose_name='Документ', upload_to='documents')