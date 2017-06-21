from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Programas)
class ProgramasModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'periodo_electivo', 'periodo_annio']
    search_fields = ['^codigo_materia', '^nombre', '^periodo_annio']

@admin.register(models.Archivo)
class ArchivoModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Solicitud)
