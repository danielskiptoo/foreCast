# Generated by Django 2.0.2 on 2018-08-12 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20180811_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='currentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.FileField(upload_to='main/static/main/data')),
                ('dateRecorded', models.DateTimeField(default=datetime.datetime(2018, 8, 12, 12, 55, 33, 918461), verbose_name='Date')),
                ('name', models.CharField(max_length=200)),
                ('cropName', models.CharField(max_length=100, null=True, verbose_name='Crop Name')),
            ],
        ),
        migrations.DeleteModel(
            name='Crop_Seasons',
        ),
        migrations.AlterField(
            model_name='csv_data',
            name='dateRecorded',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 12, 12, 55, 33, 914464), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='dateRecorded',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 12, 12, 55, 33, 917462), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='farm_production',
            name='dateRecorded',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 12, 12, 55, 33, 918461), verbose_name='Date'),
        ),
    ]
