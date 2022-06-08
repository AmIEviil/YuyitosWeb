from dataclasses import field
from django import forms
from .models import UsuarioWeb

class formLog(forms.ModelForm):
    class Meta:
        model = UsuarioWeb
        fields = ['correo','password']