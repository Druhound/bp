# -*- coding: utf-8 -*-
from django.utils import timezone
from pages.models import Document, Regulations, Category
from django.views.generic import ListView, DetailView


# Просмотр списка всех категорий нормативных документов
class AllCategoryRegulationsListView(ListView):
    model = Category
    template_name = 'Regulations_list.html'
    context_object_name = 'RegulationsList'

    def get_context_data(self, **kwargs):
        context = super(AllCategoryRegulationsListView, self).get_context_data(**kwargs)
        return context


# Просмотр списка нормативных документов
class RegulationsListView(ListView):
    template_name = 'Regulations_list.html'
    context_object_name = 'RegulationsList'

    # Фильтруем по галке публикации и фильтруем по времени публикации
    queryset = Regulations.get_published.filter(published=True).filter(datetime__lte=timezone.now())

    # Пробуем вытащить текст из категории
    def get_context_data(self, **kwargs):
        context = super(RegulationsListView, self).get_context_data(**kwargs)
        context['category'] = Category.get_published.get(slug=self.kwargs['category'])
        # context['title'] = self.queryset.filter(title=self.kwargs['category'])
        return context

    # Связывает категорию и документ в url
    def get_queryset(self):
        category_parent = Category.get_published.get(slug=self.kwargs['category'])
        queryset = self.queryset.filter(category_parent_id=category_parent.id)
        return queryset


# Детальный просмотр нормативных документов через категории
class RegulationsDetailView(DetailView):
    template_name = 'Regulations.html'
    context_object_name = 'regulations'

    # Фильтруем по галке публикации
    queryset = Regulations.get_published.filter(published=True).filter(datetime__lte=timezone.now())

    # Отвечает за вывод данных
    def get_context_data(self, **kwargs):
        context = super(RegulationsDetailView, self).get_context_data(**kwargs)
        return context

    # Связывает категорию и документ в url (Почему мы это делаем в queryset я хз)
    # Также фильтруем по времени публикации
    def get_queryset(self):
        category_parent = Category.get_published.get(slug=self.kwargs['category'])
        queryset = self.queryset.filter(category_parent_id=category_parent.id)
        return queryset


# Детальный просмотр статьи через древовидную структуру
class DocumentDetailView(DetailView):
    model = Document
    template_name = 'Document.html'

    def get_context_data(self, **kwargs):
        context = super(DocumentDetailView, self).get_context_data(**kwargs)
        return context