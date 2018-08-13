# Generated by Django 2.0.2 on 2018-08-08 12:43

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0025_auto_20180808_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='farmer',
            field=models.ForeignKey(default=17, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='dateRecorded',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 8, 15, 43, 55, 618678), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='farm_production',
            name='dateRecorded',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 8, 15, 43, 55, 618678), verbose_name='Date'),
        ),
    ]
