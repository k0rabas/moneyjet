# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 13:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160203_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='family_id',
        ),
        migrations.RemoveField(
            model_name='category',
            name='rating',
        ),
        migrations.AddField(
            model_name='transaction',
            name='family_id',
            field=models.ForeignKey(default=1111, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Family'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Category'),
        ),
    ]