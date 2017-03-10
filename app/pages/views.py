# -*- coding: utf-8 -*-
import random
from django.views.generic import ListView, DetailView
from django.http import Http404

from app.pages.models import Document, Regulations, Category
from app.currency.models import Currency


# Просмотр списка всех категорий нормативных документов
class AllCategoryRegulationsListView(ListView):
    model = Category

    template_name = 'pages/Regulations_list.html'
    context_object_name = 'category_list'
    queryset = Category.get_published.all()

    def get_context_data(self, **kwargs):
        context = super(AllCategoryRegulationsListView, self).get_context_data(**kwargs)
        return context


# Просмотр списка нормативных документов
class RegulationsListView(ListView):
    model = Category
    template_name = 'pages/Regulations_list.html'
    context_object_name = 'category_list'

    # Отвечает за вывод данных
    def get_context_data(self, **kwargs):
        context = super(RegulationsListView, self).get_context_data(**kwargs)
        # Фильтруем категории по url(category) и вытаскиваем атрибуты
        context['category'] = Category.get_published.get(slug=self.kwargs['category'])
        return context

    # Список документов
    def get_queryset(self):
        # Фильтруем документы по категории, по галке публикации, по дате публикации
        try:
            category_parent = Category.get_published.get(slug=self.kwargs['category'])
        except:
            raise Http404
        queryset = Regulations.get_published.filter(
            category_parent_id=category_parent.id)
        return queryset


# Детальный просмотр нормативных документов через категории
class RegulationsDetailView(DetailView):
    context_object_name = 'regulations'
    queryset = Regulations.get_published.all()

    def get_context_data(self, **kwargs):
        context = super(RegulationsDetailView, self).get_context_data(**kwargs)
        # Cписок избранных категорий (Псевдорандом путем выборки рандомного индекса и отсчиыванием от него 4 элемента)
        # ((Неоптимизированно))
        slice = random.random() * (Category.get_published.all().count() - 2)
        context['topicList'] = Category.get_published.all()[slice: slice + 4]
        context['news_list'] = Regulations.get_published.filter(category_parent_id=2)
        context['meta'] = self.get_object().as_meta(self.request)
        context['currency'] = Currency.objects.get(id=1)
        return context

    # Список документов которые доступны на сайте
    def get_queryset(self):
        # Фильтруем документы по категории, по галке публикации, по дате публикации
        try:
            category_parent = Category.get_published.get(slug=self.kwargs['category'])
        except:
            raise Http404
        queryset = Regulations.get_published.filter(category_parent_id=category_parent)
        return queryset

    def get_template_names(self):
        template_name = 'pages/Regulations-templates/Regulations' + self.object.templates + '.html'
        return template_name


# Детальный просмотр документов (beta)
class DocumentDetailView(DetailView):
    context_object_name = 'document'
    queryset = Document.get_published.all()

    def get_queryset(self):
        try:
            queryset = Document.get_published.filter(slug=self.kwargs['slug'])
        except:
            raise Http404
        return queryset

    def get_context_data(self, **kwargs):
        context = super(DocumentDetailView, self).get_context_data(**kwargs)
        context['meta'] = self.get_object().as_meta(self.request)
        return context

    def get_template_names(self):
        template_name = 'pages/Document-templates/Document' + self.object.templates + '.html'
        return template_name