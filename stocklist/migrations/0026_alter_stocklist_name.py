# Generated by Django 3.2.18 on 2023-04-22 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocklist', '0025_auto_20230422_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocklist',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]