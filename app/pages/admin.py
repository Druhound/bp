# coding=utf-8
from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from django.contrib import messages
from django_mptt_admin.admin import DjangoMpttAdmin

from sorl.thumbnail import get_thumbnail

from app.pages.views import Document, Regulations, Category

class DocumentAdmin(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'

    def clean_identifier(self):
        identifier = self.cleaned_data.get('identifier', False)
        if identifier and not self.data.get('parent'):
            docs = Document.objects.filter(identifier=identifier).exclude(identifier=self.instance.identifier)
            for doc in docs:
                if doc.is_root_node():
                    raise ValidationError(u'Уже есть корневой элемент с таким идентификатором!')
        return identifier

class DocumentAdminForm(DjangoMpttAdmin, forms.ModelForm):
    tree_auto_open = 0
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('title',)
    form = DocumentAdmin

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
    list_display = ('thumb', 'published', 'title', 'datetime')
    list_display_links = ('title', 'thumb')
    list_filter = ['datetime', 'category_parent']
    date_hierarchy = 'datetime'
    search_fields = ['title', 'datetime']

    def thumb(self, object):
        if object.image:
            t = get_thumbnail(object.image, "100x100", crop='center', quality=90)
            return u'<img src="%s" />' % t.url
        else:
            return u"None"

    thumb.short_description = 'Превью'
    thumb.allow_tags = True

    class Media:
        css = {
            'all': ('/media/admin.css',)
        }


admin.site.register(Document, DocumentAdminForm)
admin.site.register(Category)
admin.site.register(Regulations, RegulationsAdmin)
