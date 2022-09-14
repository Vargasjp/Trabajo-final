from django import forms

class VehiculoFormulario(forms.Form):
    marca=forms.CharField(max_length=40)
    tipo=forms.CharField(max_length=40)
    color=forms.CharField(max_length=40)
    kilometros=forms.IntegerField()


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


