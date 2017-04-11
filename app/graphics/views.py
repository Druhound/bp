from django.db.models.aggregates import Count
from django.shortcuts import render, render_to_response

from qsstats import QuerySetStats

from .models import Data


def view_func(request):
    start_date = 0
    end_date = 1000

    queryset = Data.objects.all()
    qsstats = QuerySetStats(queryset, date_field='datetime', aggregate=Count('id'))
    values = qsstats.time_series(start_date, end_date, interval='days')
    return render_to_response('template.html', {'values': values})