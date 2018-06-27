from django.contrib import admin
from .models import csv_Data,Crop_requirements
from django.contrib.admin.models import LogEntry


LogEntry.objects.all().delete()

@admin.register(csv_Data)
class csv_Data(admin.ModelAdmin):
    list_display = ('name','date_uploaded','data')

@admin.register(Crop_requirements)
class Crop_requirements(admin.ModelAdmin):
    list_display = ('crop_name','temp_requirements','rainfall_requirement','fertilizer_ha')
