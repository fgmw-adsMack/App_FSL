# Generated by Django 3.1.7 on 2021-05-14 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20210514_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
    ]