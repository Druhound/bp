# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Callback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u043e\u0435 \u043b\u0438\u0446\u043e')),
                ('telephone', models.CharField(blank=True, max_length=17, verbose_name='\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('text', models.TextField(blank=True, verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439')),
                ('url', models.CharField(blank=True, max_length=255, verbose_name='url')),
            ],
        ),
        migrations.CreateModel(
            name='CallbackSOUT2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50, verbose_name='\u0422\u0435\u043c\u0430 \u0441\u043e\u043e\u0431\u0435\u0449\u043d\u0438\u044f')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('name', models.CharField(max_length=50, verbose_name='\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u043e\u0435 \u043b\u0438\u0446\u043e')),
                ('telephone', models.CharField(max_length=17, verbose_name='\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('text', models.TextField(verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439')),
                ('document', models.FileField(upload_to='documents', verbose_name='\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442')),
            ],
        ),
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=100, verbose_name='\u0423\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440')),
                ('subject', models.CharField(max_length=100, verbose_name='\u0422\u0435\u043c\u0430')),
                ('admin_email', models.EmailField(max_length=254, verbose_name='E-mail \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430')),
                ('body', models.TextField(help_text='\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0435 \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0435:', verbose_name='\u0422\u0435\u043b\u043e')),
            ],
            options={
                'verbose_name': '\u0428\u0430\u0431\u043b\u043e\u043d \u043f\u0438\u0441\u044c\u043c\u0430',
                'verbose_name_plural': '\u0428\u0430\u0431\u043b\u043e\u043d\u044b \u043f\u0438\u0441\u0435\u043c',
            },
        ),
    ]
