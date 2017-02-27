# coding=utf-8
from __future__ import unicode_literals
import urllib
import datetime
import lxml.html as html
import requests
from xml.etree import ElementTree as ET
from django.db import models


class Currency(models.Model):
    USD = models.FloatField(verbose_name='USD', blank=True, null=True)
    EUR = models.FloatField(verbose_name='EUR', blank=True, null=True)
    Oil = models.FloatField(verbose_name='Oil', blank=True, null=True)
    datetime = models.DateField(verbose_name='Дата публикации')

    def __init__(self, *args, **kwargs):
        super(Currency, self).__init__(*args, **kwargs)
        if self.datetime < datetime.date.today():
            Currency.curr_reload(self)

    def curr_reload(self):
        try:
            page_curr = ET.parse(urllib.urlopen("http://www.cbr.ru/scripts/XML_daily.asp"))
            page_oil = requests.get('https://news.yandex.ru/quotes/1006.html')
        except:
            return self.USD, self.EUR, self.Oil

        USD_id = "R01235"
        EUR_id = "R01239"
        for line in page_curr.findall('Valute'):
            id_line = line.get('ID')
            if id_line == USD_id:
                self.USD = float(line
                                 .find('Value')
                                 .text.replace(',', '.')  # другого способа как превратить str в float я не нашел
                                 )
            if id_line == EUR_id:
                self.EUR = float(line
                                 .find('Value')
                                 .text.replace(',', '.')  # и снова
                                 )

        barrel = html.fromstring(page_oil.text)
        self.Oil = float(barrel.xpath('//td[@class="quote__value"]')[0].text_content().replace(',', '.'))

        self.datetime = datetime.date.today()
        self.save()
