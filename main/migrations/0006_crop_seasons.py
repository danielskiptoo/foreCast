# Generated by Django 2.0.2 on 2018-07-02 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20180612_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop_Seasons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_name', models.CharField(max_length=100)),
                ('maxTemp', models.CharField(max_length=50)),
                ('minTemp', models.CharField(max_length=50)),
                ('maxRainfall', models.CharField(max_length=50)),
                ('minRainfall', models.CharField(max_length=50)),
            ],
        ),
    ]
