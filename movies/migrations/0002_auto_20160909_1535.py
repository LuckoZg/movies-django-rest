# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-09 13:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='production_company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.Organization'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='score',
            field=models.IntegerField(null=True),
        ),
    ]
