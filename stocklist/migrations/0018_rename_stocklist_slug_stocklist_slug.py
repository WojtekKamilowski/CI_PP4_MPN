# Generated by Django 3.2.18 on 2023-04-14 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocklist', '0017_alter_stocklist_stocklist_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stocklist',
            old_name='stocklist_slug',
            new_name='slug',
        ),
    ]