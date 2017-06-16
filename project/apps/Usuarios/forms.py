from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        # fields = [
        #     'username',
        #     'first_name',
        #     'last_name',
        #     'email',
        # ]
        # labels = {
        #     'username': 'Nombre de Usuario',
        #     'first_name': 'Nombre',
        #     'last_name': 'Apellido',
        #     'email': 'Correo',
        # }
