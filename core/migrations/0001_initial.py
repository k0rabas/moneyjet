# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 13:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('path_to_icon', models.CharField(blank=True, max_length=20, verbose_name='Path_to_icon')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Date')),
                ('type', models.CharField(blank=True, max_length=20, verbose_name='Type')),
                ('amount', models.IntegerField(blank=True, verbose_name='Amount')),
                ('note', models.CharField(blank=True, max_length=20, verbose_name='Type')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
                'ordering': ('-date',),
            },
        ),
    ]
