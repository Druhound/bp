# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()


# Велосипед CMS
class Page(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    datetime = models.DateTimeField(verbose_name='Дата публикации')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    published = models.BooleanField(default=False, verbose_name='Опубликовано')
    text = RichTextField(null=True, blank=True, verbose_name='Текст (HTML-блок)')

    get_published = PublishedManager()

    class Meta:
        abstract = True


class Document(MPTTModel, Page):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='Children')

    def __unicode__(self):
        return '{0} {1} {2}'.format(
            self.title,
            '(опубликован)' if self.published else '',
            self.slug)

    def __init__(self, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
        if self.pk:
            self._old_slug = self.slug
        else:
            self._old_slug = None
        self._old_parent = self.parent_id

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    class MPTTMeta:
        order_insertion_by = ['title']

        def __init__(self):
            pass


class Category(Page):
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Категории нормативных документов'
        verbose_name_plural = 'Категории нормативных документов'


class Regulations(Page):
    category_parent = models.ForeignKey('Category', related_name='REG', verbose_name='Категория нормативных документов')
    file = models.FileField(verbose_name='Документ', upload_to='documents')

    def __unicode__(self):
        return self.title

    # def published(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.pub_date <= now

    class Meta:
        verbose_name = 'Нормативные документы'
        verbose_name_plural = 'Нормативные документы'
