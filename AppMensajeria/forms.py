from collections import UserList
from django import forms
from ckeditor.fields import RichTextFormField

from AppConcesionaria.forms import UserRegisterForm


class FormularioMensaje(forms.Form):

    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    destinatario=forms.ChoiceField(choices=UserRegisterForm, required=True, label="Seleccione Usuario destinatario")
    email=forms.EmailField(max_length=50)
    mensaje=RichTextFormField()
    fecha=forms.DateField()