# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-06 02:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0004_auto_20181105_2214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profesor',
            old_name='correo',
            new_name='email',
        ),
    ]
