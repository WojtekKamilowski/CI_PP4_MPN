# Generated by Django 3.2.18 on 2023-04-22 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocklist', '0029_alter_storagespace_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='storagespace',
            unique_together=set(),
        ),
    ]