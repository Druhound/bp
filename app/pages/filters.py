import django_filters

from models import Category


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='iexact_title')

    class Meta:
        model = Category
        fields = ['title', 'datetime']


class ProductFilter2(django_filters.FilterSet):
    title = django_filters.CharFilter()
    title__gt = django_filters.CharFilter(name='title', lookup_expr='gt')
    title__lt = django_filters.CharFilter(name='title', lookup_expr='lt')

    datetime = django_filters.NumberFilter(name='datetime', lookup_expr='year')
    datetime__gt = django_filters.NumberFilter(name='datetime', lookup_expr='year__gt')
    datetime__lt = django_filters.NumberFilter(name='release_date', lookup_expr='year__lt')

    class Meta:
        model = Category