# Generated by Django 3.2.18 on 2023-03-25 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocklist', '0004_auto_20230324_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocklist',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='stocklist',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
