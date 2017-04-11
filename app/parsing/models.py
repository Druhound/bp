# coding=utf-8
from __future__ import print_function
from __future__ import print_function
from __future__ import print_function
from __future__ import unicode_literals
import csv
from django.db import models
from django.utils import timezone

from app.album.models import Album


class ParsingCSV(models.Model):
    File = models.FileField(upload_to='csv/')
    CreateFile = models.BooleanField(default=False)

    def parsing(self):
        first = True
        header = None
        obj = []
        input_file = self.File
        input_file.open(mode='r')
        csv_file = csv.reader(input_file, delimiter=str(';'))
        for line in csv_file:
            if first:
                header = line
                first = False
            else:
                obj.append(dict(zip(header, line)))
        input_file.close()
        return obj

    def linking_models_with_Album(self, input_file):
        for line in input_file:
            try:
                print("##### line complete #####")
                object = Album.get_published.get(id=line.get('id'))
                object.title = line.get('title')
                object.published = line.get('published')
                for key in line:
                    if key.endswith(str(')')):
                        print("##### data #####")
                        datetime_1 = line[key].split(":")[0]
                        datetime_2 = line[key].split(":")[1]
                        print(datetime_1)
                        print(datetime_2)
                object.save()
            except:
                if self.CreateFile:
                    print('None, creating seminar')
                    object = Album.objects.create(id=line.get('id'))
                    object.title = line.get('title')
                    object.published = line.get('published')
                    object.datetime = timezone.now()
                    object.save()
                else:
                    print('None')