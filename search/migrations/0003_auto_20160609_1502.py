# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20160608_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
