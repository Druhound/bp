# -*- coding: utf-8 -*-
import random

from django.utils import timezone
from django.views.generic import ListView, DetailView

from app.pages.models import Document, Regulations, Category


# Просмотр списка всех категорий нормативных документов
class AllCategoryRegulationsListView(ListView):
    model = Category
    template_name = 'Regulations_list.html'
    context_object_name = 'category_list'
    queryset = Category.get_published.filter(datetime__lte=timezone.now())

    def get_context_data(self, **kwargs):
        context = super(AllCategoryRegulationsListView, self).get_context_data(**kwargs)

        return context


# Просмотр списка нормативных документов
class RegulationsListView(ListView):
    model = Category
    template_name = 'Regulations_list.html'
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
        category_parent = Category.get_published.get(slug=self.kwargs['category'])
        queryset = Regulations.get_published.filter(
            datetime__lte=timezone.now(),
            category_parent_id=category_parent.id)
        return queryset


# Детальный просмотр нормативных документов через категории
class RegulationsDetailView(DetailView):
    template_name = 'Regulations.html'
    context_object_name = 'regulations'

    def get_context_data(self, **kwargs):
        context = super(RegulationsDetailView, self).get_context_data(**kwargs)
        # Cписок избранных категорий (Псевдорандом путем выборки рандомного индекса и отсчиыванием от него 4 элемента)
        slice = random.random() * (Category.get_published.all().count() - 2)
        context['topicList'] = Category.get_published.all()[slice: slice + 4]
        context['news_list'] = Regulations.get_published.filter(category_parent_id=2)[:2]
        return context

    # Список документов которые доступны на сайте
    def get_queryset(self):
        # Фильтруем документы по категории, по галке публикации, по дате публикации
        category_parent = Category.get_published.get(slug=self.kwargs['category'])
        queryset = Regulations.get_published.filter(
            datetime__lte=timezone.now(),
            category_parent_id=category_parent)
        return queryset


# Детальный просмотр статьи через древовидную структуру
class DocumentDetailView(DetailView):
    model = Document
    template_name = 'Document.html'

    def get_context_data(self, **kwargs):
        context = super(DocumentDetailView, self).get_context_data(**kwargs)
        return context