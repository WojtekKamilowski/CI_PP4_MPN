# Generated by Django 3.2.18 on 2023-04-24 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocklist', '0032_alter_stockitem_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockitem',
            name='item_name',
            field=models.CharField(max_length=50),
        ),
    ]
