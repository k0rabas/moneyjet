# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 14:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.IntegerField(default=1111, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Family',
                'verbose_name_plural': 'Families',
            },
        ),
        migrations.RemoveField(
            model_name='category',
            name='path_to_icon',
        ),
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(blank=True, max_length=20, verbose_name='Icon'),
        ),
        migrations.AddField(
            model_name='category',
            name='rating',
            field=models.CharField(default=0, max_length=20, verbose_name='Icon'),
        ),
        migrations.AddField(
            model_name='category',
            name='family_id',
            field=models.ForeignKey(default=1111, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Family'),
            preserve_default=False,
        ),
    ]