# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170116_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='language',
            field=models.CharField(max_length=20),
        ),
    ]
