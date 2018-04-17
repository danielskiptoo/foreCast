from django.db import models
from datetime import date

class csv_Data(models.Model):
    data=models.FileField(upload_to='main/static/main/data')
    date_uploaded=models.DateField(auto_now_add=True, blank=True)
    name=models.CharField(max_length=200,)