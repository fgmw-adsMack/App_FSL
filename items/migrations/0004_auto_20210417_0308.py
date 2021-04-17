# Generated by Django 3.1.7 on 2021-04-17 06:08

import django.core.validators
from django.db import migrations, models
import items.models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20210416_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='user',
        ),
        migrations.AlterField(
            model_name='item',
            name='author',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='cast',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='director',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='publisher',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1800), items.models.max_value_current_year]),
        ),
    ]
