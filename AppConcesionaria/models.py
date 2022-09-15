from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Vehiculos(models.Model):
    marca=models.CharField(max_length=40)
    tipo=models.CharField(max_length=40)
    color=models.CharField(max_length=40)
    kilometros=models.IntegerField()
    imagen=models.ImageField(upload_to="imagenes", null=True, blank=True)
    fechaDePublicacion=models.DateField()

    def __str__(self):
        return self.marca+" "+str(self.tipo)


class Clientes(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    dni=models.IntegerField()

    def __str__(self):
        return self.apellido+" "+str(self.nombre)

class Empleados(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    dni=models.IntegerField()
    email=models.EmailField()
    cargo=models.CharField(max_length=40)

    def __str__(self):
         return self.apellido+" "+str(self.nombre)

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="avatares", null=True, blank=True)