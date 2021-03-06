# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 19:20
from __future__ import unicode_literals

import apps.Proceso.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Programas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_materia', models.CharField(max_length=15)),
                ('periodo_electivo', models.CharField(max_length=10)),
                ('periodo_annio', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=15)),
                ('telefono', models.CharField(max_length=18)),
                ('solvencia', models.BooleanField()),
                ('correo', models.EmailField(max_length=254)),
                ('archivo_adjunto', models.FileField(upload_to=apps.Proceso.models.path_solicitud)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_firma', models.DateTimeField(blank=True, null=True)),
                ('fecha_procesada', models.DateTimeField(blank=True, null=True)),
                ('correo_recibido', models.BooleanField(default=False)),
                ('correo_procesado', models.BooleanField(default=False)),
                ('estatus', models.CharField(choices=[('R', 'Recibido'), ('E', 'Entregado'), ('P', 'En Proceso')], default='R', max_length=10)),
                ('lista', models.FileField(blank=True, null=True, upload_to=apps.Proceso.models.path_solicitud)),
                ('usuario_creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes_creadas', to=settings.AUTH_USER_MODEL)),
                ('usuario_procesador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solicitud_procesadas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
