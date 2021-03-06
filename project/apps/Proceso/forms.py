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
            'solvencia',
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

class ProcesarForm(forms.Form):
    periodo = forms.CharField(max_length=100)
    materias = forms.CharField(max_length=100)

    def clean_periodo(self):

        data = self.cleaned_data['periodo']

        if(data.count('-') != 1):
            raise forms.ValidationError('Invalid format.')

        return data
