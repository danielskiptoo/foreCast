# Generated by Django 2.0.2 on 2018-08-09 13:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20180808_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='dateRecorded',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 9, 16, 35, 43, 453356), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='farm_production',
            name='dateRecorded',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 9, 16, 35, 43, 454355), verbose_name='Date'),
        ),
    ]