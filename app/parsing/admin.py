from django.contrib import admin
from .models import ParsingCSV


class ParsingCSVadmin(admin.ModelAdmin):
    # def save_model(self, request, obj, form, change):
    #     super(ParsingCSVadmin, self).save_model(request, obj, form, change)
    #     input_file = obj.parsing()
    #     obj.linking_models_with_Album(input_file)

    def save_model(self, request, obj, form, change):
        super(ParsingCSVadmin, self).save_model(request, obj, form, change)
        input_file = obj.parsing()
        obj.linking_models_with_UTM(input_file)

admin.site.register(ParsingCSV, ParsingCSVadmin)

