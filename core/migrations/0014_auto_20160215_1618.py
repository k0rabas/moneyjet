# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-15 14:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20160215_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category'),
        ),
    ]