# coding=utf-8
from django.views.generic import ListView, TemplateView
from django.db.models import Q
from pages.models import Regulations


class Index(TemplateView):
    template_name = 'search-form.html'


class PlaceListView(ListView):
    model = Regulations
    template_name = 'result.html'
    context_object_name = 'List'

    def get_queryset(self):
        # Получаем не отфильтрованный кверисет всех моделей
        queryset = Regulations.get_published.all()
        search = self.request.GET.get("search")
        if search:
        # Если 'q' в GET запросе, фильтруем кверисет по данным из 'q'
            return queryset.filter(Q(title__icontains=search)|
                                   Q(text__icontains=search))
        return queryset