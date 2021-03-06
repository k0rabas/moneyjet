# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-15 14:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20160215_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='family_id',
            field=models.ForeignKey(default=111111, on_delete=django.db.models.deletion.SET_DEFAULT, to='core.Family'),
        ),
        migrations.AlterField(
            model_name='family',
            name='id',
            field=models.IntegerField(default=111111, primary_key=True, serialize=False, verbose_name='FamilyID'),
        ),
    ]
