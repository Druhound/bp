from __future__ import unicode_literals

from django.db import models


class Data(models.Model):
    value_1 = models.IntegerField(verbose_name='value_1')
    value_2 = models.IntegerField(verbose_name='value_2')
    value_3 = models.IntegerField(verbose_name='value_3')
