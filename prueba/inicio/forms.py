from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuarios

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuarios
        fields = ('id_usuario','email', 'nombre', 'imagen')

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['id_usuario','email', 'nombre', 'imagen']

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['id_usuario','email', 'nombre', 'imagen']


