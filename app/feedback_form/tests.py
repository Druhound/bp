# coding=utf-8
from django.test import TestCase
from app.feedback_form.models import Callback


class CallbackTestModel(TestCase):
    def setUp(self):
        Callback.objects.create(name='Благодаров Сергей Витальевич',
                                telephone='8 (800) 555-35-35',
                                text='Позвоните мне в 8 вечера')
        Callback.objects.create(name='Иванов Петр Сергеевич',
                                telephone='8 (800) 987-55-38',
                                text='Я пришел за моим ковром')

    def SendMail(self):
        CallbackTestModel().post('/', {'name': 'Благодаров Сергей Витальевич',
                              'telephone': '8 (800) 555-35-35',
                              'text': 'Позвоните мне в 8 вечера'})
