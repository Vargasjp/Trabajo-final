from django.shortcuts import render
from django.dispatch import receiver
from .models import Mensajes
from .forms import MensajeForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class MensajeLista(LoginRequiredMixin, ListView):

    model=Mensajes
    template_name="AppMensajes/mensajeLista.html"

class MensajeDetalle(LoginRequiredMixin, DetailView):

    model=Mensajes
    template_name="AppMensajes/mensajeDetalle.html"

class CrearMensaje(LoginRequiredMixin, CreateView):

    model=Mensajes
    success_url="/messages/"
    fields = ['remitente','recibido', 'mensaje', 'fecha', 'es leido']


class EliminarMensaje(LoginRequiredMixin, DeleteView):

    model=Mensajes
    success_url = "/messages/"