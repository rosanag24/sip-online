# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-06 02:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0005_auto_20181105_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='jefe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jefe_de', to='gestion.Profesor'),
        ),
    ]