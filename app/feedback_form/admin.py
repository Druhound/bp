from django.contrib import admin
from .models import CallbackSOUT2, EmailTemplate



class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'subject')

admin.site.register(CallbackSOUT2)
admin.site.register(EmailTemplate, EmailTemplateAdmin)

