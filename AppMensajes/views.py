from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from AppConcesionaria.models import Avatar
from AppMensajes.forms import *
from AppMensajes.models import *
from django.views.generic.list import ListView
from django.utils import timezone
# Create your views here.

def crearMensaje(request):
    if request.method=="POST":
        form= FormularioMensaje(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            destinatario=info["destinatario"]
            email=info["email"]
            mensaje=info["mensaje"]
            fecha=info["fecha"]
            msj= CrearMensaje(nombre=nombre, apellido=apellido, destinatario=destinatario, email=email, mensaje=mensaje, fecha=fecha)
            msj.save()
            return render (request, "AppConcesionaria/inicio.html", {"mensaje": "Mensaje Creado"})
        else:
            return render (request, "AppConcesionaria/inicio.html", {"mensaje": "Error"})
    else:
        form=FormularioMensaje()
    return render(request, "AppMensajes/crearMensaje.html", {"formulario":form})

def leerMensajes(request):
    mensajes=CrearMensaje.objects.all()
    contexto={"mensajes":mensajes}
    return render(request, "AppMensajes/leerMensajes.html", contexto)
# Create your views here.
def verMensaje(request,id):
    msj=CrearMensaje.objects.get(id=id)
    return render(request, "AppMensajes/verMensaje.html", { "mensaje":msj})