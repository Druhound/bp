# coding=utf-8
from django.contrib import admin
from sorl.thumbnail import get_thumbnail

from .models import Photo, Album


class PhotoInLine(admin.StackedInline):
    list_display = ('thumb',)
    model = Photo
    extra = 3

    def thumb(self, object):
        if object.image:
            t = get_thumbnail(object.image, "100x100", crop='center', quality=90)
            return u'<img src="%s" />' % t.url
        else:
            return u"None"

    thumb.short_description = 'Превью'
    thumb.allow_tags = True


class AlbumAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Main', {
            'fields': ('published', 'title', 'datetime')
        }),
    )
    inlines = [PhotoInLine]


admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo)
