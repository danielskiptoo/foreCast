# Generated by Django 2.0.2 on 2018-08-06 09:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20180805_2321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expenses',
            old_name='farm_Id',
            new_name='farm',
        ),
        migrations.RenameField(
            model_name='farm_production',
            old_name='farm_id',
            new_name='farm',
        ),
        migrations.AlterField(
            model_name='expenses',
            name='dateRecorded',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 6, 12, 12, 23, 43688), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='farm_production',
            name='dateRecorded',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 6, 12, 12, 23, 44687), verbose_name='Date'),
        ),
    ]
