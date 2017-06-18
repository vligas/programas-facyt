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
            'solvencia',
            'correo',
            'archivo_adjunto',
        ]

        label ={
            'nombre':'Nombre',
            'apellido':'Apellido',
            'cedula':'Cédula',
            'telefono':'Teléfono',
            'solvencia':'solvencia',
            'correo':'Correo',
            'archivo_adjunto':'Archivo',
        }
