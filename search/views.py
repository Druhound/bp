# coding=utf-8
from django.views.generic import ListView, TemplateView
from django.db.models import Q
from pages.models import Regulations


class PlaceListView(ListView):
    model = Regulations
    template_name = 'search-form.html'
    context_object_name = 'List'

    def get_queryset(self):
        search = self.request.GET.get("pages")
        if search:
            # Получаем не отфильтрованный список моделей "Нормативные документы"
            queryset = Regulations.get_published.all()
            # Если 'pages' в GET запросе, фильтруем кверисет по данным из 'pages'
            return queryset.filter(Q(title__icontains=search) |
                                   Q(text__icontains=search))
        else:
            return self.queryset
