# coding=utf-8
from __future__ import unicode_literals

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone
from meta.models import ModelMeta

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(published=True, datetime__lte=timezone.now())


class PublishedModel(models.Model):
    published = models.BooleanField(default=False, verbose_name=u'Опубликовано')
    datetime = models.DateTimeField(verbose_name='Дата публикации', default=timezone.now())

    objects = models.Manager()
    get_published = PublishedManager()

    class Meta:
        abstract = True


class Album(PublishedModel, models.Model):
    title = models.CharField(max_length=255, verbose_name='Название альбома')

    title_page = models.CharField(max_length=170, blank=True)
    description_page = models.TextField(blank=True)
    keywords_page = models.TextField(blank=True)

    def __unicode__(self):
        return self.title

    _metadata = {
        'title': 'title_page',
        'description': 'description_page',
        'keywords': 'keywords_page',
    }

    def __unicode__(self):
        return self.title


class Photo(models.Model):
    datetime_1 = models.DateField(verbose_name='Дата начала', default=timezone.now())
    datetime_2 = models.DateField(verbose_name='Дата конца', default=timezone.now())
    Album = models.ForeignKey('Album', related_name='Album', verbose_name='Альбом', on_delete=models.CASCADE)
