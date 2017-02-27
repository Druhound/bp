# coding=utf-8
from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from django.contrib import messages
from django_mptt_admin.admin import DjangoMpttAdmin

from sorl.thumbnail import get_thumbnail


from app.pages.views import Document, Regulations, Category


class DocumentAdminForm(forms.ModelForm):
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


class DocumentAdmin(DjangoMpttAdmin, forms.ModelForm, admin.ModelAdmin):
    tree_auto_open = 0
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('title',)
    form = DocumentAdminForm

    fieldsets = (
        (None, {
            'fields': ('published', 'title', 'identifier',  'templates', 'text', 'datetime'),
        }),
        ('SEO', {
            'fields': ('title_page', 'description_page', 'keywords_page')
        }),
    )

    def save_model(self, request, obj, form, change):
        super(DocumentAdmin, self).save_model(request, obj, form, change)
        if obj.identifier != obj._old_identifier or obj._old_parent != obj.parent:
            descendants = obj.get_root().get_descendants(include_self=True)
            for descendant in descendants:
                descendant.slug = u'' + u'/'.join([doc.identifier for doc in descendant.get_ancestors(include_self=True)]) + u'/'
                descendant.save()
            messages.info(request, u"У {} документов обновлен Slug".format(len(descendants)))


class RegulationsAdmin(admin.ModelAdmin):
    list_display = ('thumb', 'published', 'title', 'datetime')
    list_display_links = ('title', 'thumb')
    list_filter = ['datetime', 'category_parent']
    date_hierarchy = 'datetime'
    search_fields = ['title', 'datetime']

    fieldsets = (
        (None, {
            'fields': ('published', 'title', 'slug', 'data', 'templates', 'text', 'datetime')
        }),
        ('SEO', {
            'classes': ('collapse',),
            'fields': ('title_page', 'description_page', 'keywords_page'),
        }),
    )

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


admin.site.register(Document, DocumentAdmin)
admin.site.register(Category)
admin.site.register(Regulations, RegulationsAdmin)
