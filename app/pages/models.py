# coding=utf-8
from __future__ import unicode_literals

from django.utils import timezone
from django.db import models
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey
import django_filters
from meta.models import ModelMeta


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(published=True, datetime__lte=timezone.now())


class PublishedModel(models.Model):
    published = models.BooleanField(default=False, verbose_name=u'Опубликовано')

    objects = models.Manager()
    get_published = PublishedManager()

    class Meta:
        abstract = True


# Велосипед CMS
class Page(ModelMeta, PublishedModel, models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    datetime = models.DateTimeField(verbose_name='Дата публикации')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    text = RichTextField(null=True, blank=True, verbose_name='Текст (HTML-блок)')

    title_page = models.CharField(max_length=170, blank=True)
    description_page = models.TextField(blank=True)
    keywords_page = models.TextField(blank=True)

    _metadata = {
        'title': 'title_page',
        'description': 'description_page',
        'keywords': 'keywords_page',
    }

    class Meta:
        abstract = True


class Document(MPTTModel, Page):
    TEMPLATES = (
        ('-1', 'template-1'),
        ('-2', 'template-2'),
        ('-3', 'template-3'),
        ('-4', 'template-4'),
    )
    templates = models.CharField(max_length=15, verbose_name='Шаблон', choices=TEMPLATES, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='Children', on_delete=models.CASCADE)
    identifier = models.CharField(max_length=255, verbose_name='Идентификатор для url')

    def __unicode__(self):
        return '{0} {1} {2}'.format(
            self.title,
            '(опубликован)' if self.published else '',
            self.slug)

    def __init__(self, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
        if self.pk:
            self._old_identifier = self.identifier
        else:
            self._old_identifier = None
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

    def get_absolute_url(self):
        return reverse('pages:list', args=[self.slug])

    class Meta:
        verbose_name = 'Категория страницы'
        verbose_name_plural = 'Категории страниц'


class Regulations(Page):
    TEMPLATES = (
        ('-1', 'template-1'),
        ('-2', 'template-2'),
        ('-3', 'template-3'),
        ('-4', 'template-4'),
    )
    templates = models.CharField(max_length=15, verbose_name='Шаблон', choices=TEMPLATES, blank=True)
    category_parent = models.ForeignKey('Category', related_name='REG', verbose_name='Категория нормативных документов', on_delete=models.CASCADE)
    file = models.FileField(verbose_name='Документ', upload_to='documents')
    image = models.ImageField(blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        category = self.category_parent.slug
        return reverse('pages:detail', kwargs={'category': category, 'slug': self.slug})

    class Meta:
        verbose_name = 'Нормативные документы'
        verbose_name_plural = 'Нормативные документы'


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Regulations
        fields = {
            'title' : ['icontains'],
        }