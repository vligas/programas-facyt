from django import forms
from . import models

class SolicitudForm(forms.ModelForm):


    class Meta:
        model = models.Solicitud()

        fields = [
            'nombre',
            'apellido',
            'cedula',
            'telefono',
            'solvencia',
            'correo',
            'archivo_adjunto',
        ]
