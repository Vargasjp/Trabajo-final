from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class VehiculoFormulario(forms.Form):
    marca=forms.CharField(max_length=40)
    tipo=forms.CharField(max_length=40)
    color=forms.CharField(max_length=40)
    kilometros=forms.IntegerField()
    imagen=forms.ImageField(label="Imagen")
    fechaDePublicacion=forms.DateField()


class EmpleadoForm(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    dni=forms.IntegerField()
    email=forms.EmailField()
    cargo=forms.CharField(max_length=40)

class ClienteForm(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    email=forms.EmailField()
    dni=forms.IntegerField()


class UserRegisterForm(UserCreationForm):
    username=forms.CharField()
    email=forms.EmailField()
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
            model = User
            fields = ["username", "email", "password1", "password2"]
            help_texts = {k:"" for k in fields}

class UserEditform(UserCreationForm):
    email=forms.EmailField(label="Modificar E-Mail")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label="Modificar Nombre")
    last_name=forms.CharField(label="Modificar Apellido")

    class Meta:
        model=User
        fields=["email", "password1", "password2", "first_name", "last_name"] 
        help_texts={k:"" for k in fields}