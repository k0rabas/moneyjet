# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-16 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20160216_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='pin',
            field=models.CharField(default=0, max_length=4, verbose_name='PIN'),
        ),
    ]