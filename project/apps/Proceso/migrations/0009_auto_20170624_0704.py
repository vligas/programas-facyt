# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proceso', '0008_auto_20170624_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]