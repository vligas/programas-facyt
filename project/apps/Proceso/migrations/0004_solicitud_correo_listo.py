# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-20 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proceso', '0003_programas_solicitudes'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='correo_listo',
            field=models.BooleanField(default=False),
        ),
    ]