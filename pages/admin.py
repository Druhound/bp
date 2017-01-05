# coding=utf-8
from django.contrib import admin
from django import forms
from django_mptt_admin.admin import DjangoMpttAdmin
from django.contrib import messages
from pages.models import Document, Regulations, Category


class DocumentAdminForm(DjangoMpttAdmin, forms.ModelForm):
    tree_auto_open = 0
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('title',)
    def save_model(self, request, obj, form, change):
        super(DocumentAdminForm, self).save_model(request, obj, form, change)
        if obj.slug != obj._old_slug or obj._old_parent != obj.parent:
            descendants = obj.get_descendants(include_self=True)
            for descendant in descendants:
                descendant.slug = ''.join([doc.slug for doc in descendant.get_ancestors(include_self=True)]) + u'/'
                descendant.save()
            messages.info(request, u"У {} документов обновлен URL".format(len(descendants)))

    class Meta:
        model = Document
        fields = '__all__'


class RegulationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published', 'category_parent', 'datetime',)

admin.site.register(Document, DocumentAdminForm)
admin.site.register(Category)
admin.site.register(Regulations,RegulationsAdmin)