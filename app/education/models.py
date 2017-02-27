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


class Education(ModelMeta, MPTTModel, PublishedModel):
    TEMPLATES = (
        ('-program', 'Программа'),
        ('-category', 'Категория')
    )
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='Children', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    identifier = models.CharField(max_length=255, verbose_name='Идентификатор для url')
    datetime = models.DateTimeField(verbose_name='Дата публикации')
    templates = models.CharField(max_length=15, verbose_name='Шаблон', choices=TEMPLATES)

    # Текстовые блоки
    # -- Описание категории
    module1 = RichTextField(blank=True, verbose_name='Описание')

    # -- Черный блок
    module2 = RichTextField(blank=True, verbose_name='Описание')
    module3 = models.BooleanField(default=True, verbose_name='Отобразить кнопку "Очно"?')
    module4 = models.BooleanField(default=True, verbose_name='Отобразить кнопку "Заочно"?')

    # -- Синий блок
    module5 = models.CharField(blank=True, max_length=100, verbose_name='Время')
    module6 = models.CharField(blank=True, max_length=100, verbose_name='Ссылка на 1-е изображение')
    module7 = models.CharField(blank=True, max_length=100, verbose_name='Ссылка на 2-е изображение')

    # -- Основной блок
    module8 = RichTextField(blank=True, verbose_name='Описание курса')
    module9 = RichTextField(blank=True, verbose_name='Программа курса')
    module10 = RichTextField(blank=True, verbose_name='Причины пройти обучение')
    module11 = RichTextField(blank=True, verbose_name='Штраф')
    module12 = RichTextField(blank=True, verbose_name='Законодательство')

    # -- Также рекомендуем
    module13 = RichTextField(blank=True, verbose_name='Также рекомендуем')
    # end

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
        super(Education, self).__init__(*args, **kwargs)
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