# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-19 00:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20160217_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon_face',
            field=models.CharField(blank=True, max_length=20, verbose_name='Icon Face'),
        ),
    ]
