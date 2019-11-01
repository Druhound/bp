# coding=utf-8
from django.contrib import admin
from sorl.thumbnail import get_thumbnail

from .models import Photo, Album


class PhotoInLine(admin.StackedInline):
    list_display = ('thumb',)
    model = Photo
    extra = 3


class AlbumAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Main', {
            'fields': ('published', 'title', 'datetime', 'date')
        }),
    )
    inlines = [PhotoInLine]


admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo)
