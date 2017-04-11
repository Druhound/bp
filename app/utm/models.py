# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Utm(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Название')
    description = models.CharField(blank=True, max_length=200, verbose_name='Описание')

    def __unicode__(self):
        return self.name