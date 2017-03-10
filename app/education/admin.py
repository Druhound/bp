# coding=utf-8
from django.contrib import admin
from app.education.views import Education
from django import forms
from django.core.exceptions import ValidationError
from django_mptt_admin.admin import DjangoMpttAdmin


class EducationAdminForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

    def clean_identifier(self):
        identifier = self.cleaned_data.get('identifier', False)
        if identifier and not self.data.get('parent'):
            docs = Education.objects.filter(identifier=identifier).exclude(identifier=self.instance.identifier)
            for doc in docs:
                if doc.is_root_node():
                    raise ValidationError(u'Уже есть корневой элемент с таким идентификатором!')
        return identifier


class Media:
    css = {
        'all': ('/static/custom/admin_education.css',)
    }


class EducationAdmin(DjangoMpttAdmin, admin.ModelAdmin):
    tree_auto_open = 0
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('title',)
    form = EducationAdminForm

    fieldsets = (
        ('Основное', {
            'fields': ('published', 'title', 'parent', 'identifier',  'templates', 'datetime'),
        }),
        ('Категория', {
            'classes': ('collapse',),
            'fields': ('module1',)
        }),
        ('Программы', {
            'classes': ('collapse',),
            'fields': ('module3', 'module4', 'module2', 'module5',
                       'module6', 'module7', 'module8', 'module9',
                       'module10', 'module11', 'module12', 'module13')
        }),
        ('Цены', {
            'classes': ('inlines',),
            'fields': (('price_msc', 'price_sbp', 'price_oth'), )
        }),
        ('SEO', {
            'classes': ('collapse',),
            'fields': ('title_page', 'description_page', 'keywords_page')
        }),
    )

    def save_model(self, request, obj, form, change):
        super(EducationAdmin, self).save_model(request, obj, form, change)
        if obj.identifier != obj._old_identifier or obj._old_parent != obj.parent:
            descendants = obj.get_root().get_descendants(include_self=True)
            for descendant in descendants:
                descendant.slug = u'' + u'/'.join([doc.identifier for doc in descendant.get_ancestors(include_self=True)]) + u'/'
                descendant.save()


admin.site.register(Education, EducationAdmin)
