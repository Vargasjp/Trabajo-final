from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from AppMensajeria.forms import *
from AppMensajeria.models import *
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.

class CrearMensaje(LoginRequiredMixin, CreateView):

    model=Mensaje
    success_url=reverse_lazy("leerMensajes")
    fields = ['fecha','nombre', 'apellido', 'destinatario', 'mensaje', 'email']

@login_required
def leerMensajes(request):
    destinatario = request.user
    mensajes=Mensaje.objects.filter(destinatario=destinatario)
    contexto={"mensajes":mensajes}
    return render(request, "AppMensajeria/leerMensajes.html", contexto)

@login_required
def verMensaje(request,id):
    msj=Mensaje.objects.get(id=id)
    return render(request, "AppMensajeria/verMensaje.html", { "mensaje":msj})