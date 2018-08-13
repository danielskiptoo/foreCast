from django.contrib import admin
from .models import csv_Data, Crop_requirements, farm_production, currentData, Expenses, Farm
from django.contrib.admin.models import LogEntry


LogEntry.objects.all().delete()

@admin.register(csv_Data)
class csv_Data(admin.ModelAdmin):
    list_display = ('name', 'maxCropYield','minCropYield','cropName','dateRecorded','data')


@admin.register(currentData)
class currentData(admin.ModelAdmin):
    list_display = ('name','cropName','dateRecorded','data')

@admin.register(Crop_requirements)
class Crop_requirements(admin.ModelAdmin):
    list_display = ('crop_name','temp_max','temp_min','max_rainfall','min_rainfall', 'min_expected_acre', 'max_expected_acre', 'fertilizer_ha')

# @admin.register(Crop_Seasons)
# class Crop_Seasons(admin.ModelAdmin):
#     list_display = ('period_name','maxTemp','minTemp','avgRainfall')

@admin.register(farm_production)
class farm_production(admin.ModelAdmin):
    list_display = ('farm','production_amount')

@admin.register(Expenses)
class Expenses(admin.ModelAdmin):
    list_display = ('farm','amount','description','dateRecorded')

@admin.register(Farm)
class Farm(admin.ModelAdmin):
    list_display = ('name','type','size','location','farmer')


