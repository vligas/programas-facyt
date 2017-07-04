from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Programas)
class ProgramasModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'periodo_electivo', 'periodo_annio', 'file']
    search_fields = ['codigo_materia', 'nombre', 'periodo_annio']

    def file(self, obj):
        if obj.archivo:
            return '{}'.format(obj.archivo.documento.name)
        else:
            return 'None'

@admin.register(models.Archivo)
class ArchivoModelAdmin(admin.ModelAdmin):
    search_fields = ['documento']


admin.site.register(models.Solicitud)
