# Generated by Django 3.2.18 on 2023-05-19 07:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocklist', '0038_auto_20230518_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storagespace',
            name='temp',
            field=models.IntegerField(default=21, validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(-30)]),
        ),
    ]
