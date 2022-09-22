from django import forms
from ckeditor.fields import RichTextFormField


class FormularioMensaje(forms.Form):

    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    destinatario=forms.CharField(max_length=40)
    email=forms.EmailField(max_length=50)
    mensaje=RichTextFormField()
    fecha=forms.DateField()
    