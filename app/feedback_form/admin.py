from django.contrib import admin
from .models import Callback, EmailTemplate


class CallbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'telephone', 'text')
    fields = ('name', 'telephone', 'text', 'title', 'url')


class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'subject')

admin.site.register(Callback, CallbackAdmin)
admin.site.register(EmailTemplate, EmailTemplateAdmin)

