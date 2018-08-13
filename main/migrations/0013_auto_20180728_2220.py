# Generated by Django 2.0.2 on 2018-07-28 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20180727_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crop_requirements',
            name='expected_yield_acre',
        ),
        migrations.RemoveField(
            model_name='crop_requirements',
            name='rainfall_requirement',
        ),
        migrations.RemoveField(
            model_name='crop_requirements',
            name='temp_requirements',
        ),
        migrations.AddField(
            model_name='crop_requirements',
            name='max_expected_acre',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name=' Min Expected Yield/Acre'),
        ),
        migrations.AddField(
            model_name='crop_requirements',
            name='max_rainfall',
            field=models.CharField(default='', max_length=50, verbose_name='Max Rainfall'),
        ),
        migrations.AddField(
            model_name='crop_requirements',
            name='min_expected_acre',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Max Expected Yield/Acre'),
        ),
        migrations.AddField(
            model_name='crop_requirements',
            name='min_rainfall',
            field=models.CharField(default='', max_length=50, verbose_name='Min Rainfall'),
        ),
        migrations.AddField(
            model_name='crop_requirements',
            name='temp_max',
            field=models.CharField(default='', max_length=50, verbose_name='Max Temperature'),
        ),
        migrations.AddField(
            model_name='crop_requirements',
            name='temp_min',
            field=models.CharField(default='', max_length=50, verbose_name=' Min Temperature'),
        ),
        migrations.AlterField(
            model_name='crop_requirements',
            name='crop_name',
            field=models.CharField(default='', max_length=70, verbose_name='Crop'),
        ),
        migrations.AlterField(
            model_name='crop_requirements',
            name='fertilizer_ha',
            field=models.CharField(default='', max_length=100, verbose_name='Fertilizer/Ha'),
        ),
    ]