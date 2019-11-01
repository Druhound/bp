from __future__ import unicode_literals
import csv
from django.db import models

from app.pages.models import Regulations
from app.utm.models import Utm

class ParsingCSV(models.Model):
    File = models.FileField(upload_to='csv/')
    CreateFile = models.BooleanField(default=False)

    def parsing(self):
        first = True
        header = None
        obj = []
        file = self.File.url
        with open('/home/druhound/virtualprojects/source/bp/files' + file, 'r') as f:
            csv_file = csv.reader(f, delimiter=str(','))
            for line in csv_file:
                if first:
                    header = line
                    first = False
                else:
                    obj.append(dict(zip(header, line)))
            f.close()
        return obj

    def linking_models_with_UTM(self, input_file):
        for line in input_file:
            try:
                print("##### line complete #####")
                object = Utm.get_published.get(name=line.get('name'))
                object.description = line.get('description')
                object.save()
            except:
                if self.CreateFile:
                    print('None, creating UTM')
                    a = Utm.objects.create(name=line.get('name'))
                    a.description = line.get('description')
                    a.save()
                else:
                    print('None')

# class ParsingCSV(models.Model):
#     File = models.FileField(upload_to='csv/')
#     CreateFile = models.BooleanField(default=False)
#
#     def parsing(self):
#         first = True
#         header = None
#         obj = []
#         file = self.File.url
#         with open('/home/druhound/virtualprojects/source/bp/files' + file, 'r') as f:
#             csv_file = csv.reader(f, delimiter=str(';'))
#             for line in csv_file:
#                 if first:
#                     header = line
#                     first = False
#                 else:
#                     obj.append(dict(zip(header, line)))
#             f.close()
#         return obj
#
#     def linking_models_with_Album(self, input_file):
#         for line in input_file:
#             # try:
#                 print("##### line complete #####")
#                 object = Regulations.get_published.get(id=line.get('id'))
#                 object.title = line.get('title')
#                 object.published = line.get('published')
#                 line.pop('id')
#                 line.pop('title')
#                 line.pop('published')
#                 print(line)
#                 object.date = line
#                 object.save()
#             # except:
#             #     if self.CreateFile:
#             #         print('None, creating seminar')
#             #         with Album.objects.create(id=line.get('id')) as object:
#             #             object.title = line.get('title')
#             #             object.published = line.get('published')
#             #             object.datetime = timezone.now()
#             #             object.save()
#             #     else:
#             #         print('None')