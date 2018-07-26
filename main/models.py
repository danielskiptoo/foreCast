from django.db import models
from datetime import date
from django.contrib.auth.models import User

FARM_TYPES = (
    ('wheat','Wheat'),
    ('maize','Maize'),
)

class csv_Data(models.Model):
    data=models.FileField(upload_to='main/static/main/data')
    date_uploaded=models.DateField(auto_now_add=True, blank=True)
    name=models.CharField(max_length=200,)

class Crop_requirements(models.Model):
    crop_name=models.CharField('Crop',max_length=70,)
    temp_requirements=models.CharField('Temperature Requirements',max_length=50)
    rainfall_requirement=models.CharField('Rainfall Requirements',max_length=50)
    fertilizer_ha=models.CharField( 'Fertilizer/Ha',max_length=100)

class Crop_Seasons(models.Model):
    period_name=models.CharField(max_length=100,blank=True,default='')
    maxTemp=models.CharField(max_length=50,blank=True,default='')
    minTemp=models.CharField(max_length=50, blank=True,default='')
    avgRainfall=models.CharField(max_length=50,blank=True,default='')
    avgTemp=models.CharField(max_length=50,default='', blank=True)

    def __str__(self):
        return self.period_name + ' '+ self.avgRainfall

class Farm(models.Model):
    name=models.CharField(max_length=100,default='',blank=True)
    type=models.CharField(default='',blank=True,choices=FARM_TYPES, max_length=8)
    size=models.CharField(max_length=50,blank=True,default='')
    farmer=models.ForeignKey(User, on_delete=models.CASCADE)

