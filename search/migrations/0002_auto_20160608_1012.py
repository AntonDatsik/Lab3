# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='value',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
