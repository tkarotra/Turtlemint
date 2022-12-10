from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class ModelField(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['make', 'model', 'year', 'engine_fuel_type', 
    'engine_hp', 'engine_cylinders', 'transmission_type', 
    'driven_wheels', 'no_of_doors', 'market_category', 
    'vehicle_size', 'vehicle_style', 'highway_mpg', 'city_mpg', 
    'msrp']

class CompanyField(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Company, CompanyField)
admin.site.register(Model, ModelField)