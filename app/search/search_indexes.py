from __future__ import unicode_literals

from django.utils import timezone
from haystack import indexes

from app.pages.models import Regulations


class RegulationsIndex(indexes.SearchIndex, indexes.Indexable):
    title = indexes.CharField(model_attr='title')
    text = indexes.CharField(model_attr='text', document=True, use_template=True)

    def get_model(self):
        return Regulations

    def index_queryset(self, using=None):
        return self.get_model().get_published.filter(datetime__lte=timezone.now())