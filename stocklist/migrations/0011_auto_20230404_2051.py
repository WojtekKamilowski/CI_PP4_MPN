# Generated by Django 3.2.18 on 2023-04-04 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocklist', '0010_stockitem_item_updated_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storagespace',
            name='stocklist',
        ),
        migrations.DeleteModel(
            name='Stockitem',
        ),
        migrations.DeleteModel(
            name='Storagespace',
        ),
    ]