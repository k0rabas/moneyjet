# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-19 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_transaction_family_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='pin',
            field=models.CharField(default='0000', max_length=4, verbose_name='PIN'),
        ),
    ]