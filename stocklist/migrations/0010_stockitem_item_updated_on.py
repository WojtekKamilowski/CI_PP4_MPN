# Generated by Django 3.2.18 on 2023-04-04 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocklist', '0009_stocklist_list_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockitem',
            name='item_updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
