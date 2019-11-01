# coding=utf-8
from __future__ import unicode_literals
from django.utils import timezone
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey
from meta.models import ModelMeta
from django.db import models

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(published=True, datetime__lte=timezone.now())


class PublishedModel(models.Model):
    published = models.BooleanField(default=False, verbose_name=u'Опубликовано')

    objects = models.Manager()
    get_published = PublishedManager()

    class Meta:
        abstract = True


class News(ModelMeta, PublishedModel):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    datetime = models.DateTimeField(verbose_name='Дата публикации')

    # Мета
    title_page = models.CharField(max_length=170, blank=True)
    description_page = models.TextField(blank=True)
    keywords_page = models.TextField(blank=True)

    def __unicode__(self):
        return '{0} {1} {2}'.format(
            self.title,
            '(опубликован)' if self.published else '',
            self.slug)

    def __init__(self, *args, **kwargs):
        super(News, self).__init__(*args, **kwargs)
        if self.pk:
            self._old_identifier = self.identifier
        else:
            self._old_identifier = None
        self._old_parent = self.parent_id

    _metadata = {
        'title': 'title_page',
        'description': 'description_page',
        'keywords': 'keywords_page',
    }

    class Meta:
        verbose_name = 'Документ учебного центра'
        verbose_name_plural = 'Документы учебного центра'

    class MPTTMeta:
        order_insertion_by = ['title']

        def __init__(self):
            pass