from django import forms
from . import models

class SolicitudForm(forms.ModelForm):


    class Meta:
        model = models.Solicitud # ERROR AQUI NO SE INSTANCIA

        fields = [
            'nombre',
            'apellido',
            'cedula',
            'telefono',
            'correo',
            'archivo_adjunto',
        ]

        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'cedula': 'Cedula',
            'correo': 'Correo',
            'archivo_adjunto': 'Archivo'
        }
