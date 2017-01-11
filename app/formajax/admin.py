from django.contrib import admin
from .models import OrderService, Callback, CallbackSOUT, CallbackExperts


class OrderServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'email','telephone', 'creation_date')


class CallbackSOUTAdmin(admin.ModelAdmin):
    list_display = ('name', 'telephone', 'creation_date')


class CallbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'telephone', 'text', 'creation_date')


class CallbackExpertsAdmin(admin.ModelAdmin):
    list_display = ('name', 'telephone', 'creation_date')

admin.site.register(OrderService, OrderServiceAdmin)
admin.site.register(CallbackSOUT, CallbackSOUTAdmin)
admin.site.register(Callback, CallbackAdmin)
admin.site.register(CallbackExperts, CallbackExpertsAdmin)

