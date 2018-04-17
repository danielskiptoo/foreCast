from django.contrib import admin
from .models import csv_Data

@admin.register(csv_Data)
class csv_Data(admin.ModelAdmin):
    list_display = ('name','date_uploaded','data')
