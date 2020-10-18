
from django import forms
from django.forms import ModelChoiceField
#from martor.fields import MartorFormField


class AuthForm(forms.Form):
    usuario = forms.CharField(label="Nombre de usuario", required=True, initial="usuario", help_text="Usuario uniandes")
    password = forms.CharField(
        label="Password", required=True, initial="password", help_text="Password de la plataforma"
    )
