# Generated by Django 2.0.2 on 2018-04-17 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180417_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv_data',
            name='data',
            field=models.FileField(upload_to='main/media/main/data'),
        ),
    ]
