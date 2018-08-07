
from django.db import models
from datetime import date, datetime
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
    crop_name=models.CharField('Crop',max_length=70,default='')
    temp_min=models.CharField(' Min Temperature',max_length=50,default='')
    temp_max = models.CharField('Max Temperature', max_length=50,default='')
    min_rainfall = models.CharField('Min Rainfall', max_length=50,default='')
    max_rainfall=models.CharField('Max Rainfall',max_length=50, default='')
    fertilizer_ha=models.CharField( 'Fertilizer/Ha',max_length=100,default='')
    min_expected_acre=models.DecimalField('Max Expected Yield/Acre',max_digits=8, decimal_places=2,default=0)
    max_expected_acre = models.DecimalField(' Min Expected Yield/Acre', max_digits=8, decimal_places=2, default=0)

class Crop_Seasons(models.Model):
    period_name=models.CharField(max_length=100,blank=True,default='')
    maxTemp=models.CharField(max_length=50,blank=True,default='')
    minTemp=models.CharField(max_length=50, blank=True,default='')
    avgRainfall=models.CharField(max_length=50,blank=True,default='')
    avgTemp=models.CharField(max_length=50,default='', blank=True)

    def __str__(self):
        return self.period_name + ' '+ self.avgRainfall

class Farm(models.Model):
    name=models.CharField(max_length=100)
    type=models.CharField(default='',choices=FARM_TYPES, max_length=8)
    size=models.CharField(max_length=50,default='')
    farmer=models.ForeignKey(User, on_delete=models.CASCADE)

class Expenses(models.Model):
    farm=models.ForeignKey(Farm,on_delete=models.CASCADE)
    def __str__(self):
        return self.farm
    amount=models.DecimalField('Amount',max_digits=8, decimal_places=2)
    description=models.CharField('Description',max_length=300,default='')
    dateRecorded=models.DateTimeField('Date', default=datetime.now())




class farm_production(models.Model):
    YEAR_CHOICES = []
    for r in range(1980, (datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))
    farm=models.ForeignKey(Farm,on_delete=models.CASCADE)
    def __str__(self):
        return self.farm
    year = models.IntegerField('Year', choices=YEAR_CHOICES, default=datetime.now().year)
    production_amount=models.DecimalField('Production Amount in Kgs',decimal_places=2, max_digits=32)
    dateRecorded = models.DateTimeField('Date', default=datetime.now())



