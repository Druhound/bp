# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField


class Review(models.Model):
    name = models.CharField(verbose_name='Отзыв', max_length=50),
    text = RichTextField(verbose_name='Отзыв'),
    datetime = models.DateTimeField()

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
