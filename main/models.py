from django.db import models
from datetime import date

class csv_Data(models.Model):
    data=models.FileField(upload_to='main/static/main/data')
    date_uploaded=models.DateField(auto_now_add=True, blank=True)
    name=models.CharField(max_length=200,)

class Crop_requirements(models.Model):
    crop_name=models.CharField('Crop',max_length=70,)
    temp_requirements=models.CharField('Temperature Requirements',max_length=50)
    rainfall_requirement=models.CharField('Rainfall Requirements',max_length=50)
    fertilizer_ha=models.CharField( 'Fertilizer/Ha',max_length=100)

