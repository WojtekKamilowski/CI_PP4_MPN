# Generated by Django 3.2.18 on 2023-04-02 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocklist', '0007_auto_20230402_0907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storagespace',
            old_name='str_name',
            new_name='storage_name',
        ),
    ]