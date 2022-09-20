from django.shortcuts import render
from django.dispatch import receiver
from .models import Mensajes
from .forms import MensajeForm
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class mensajeLista(LoginRequiredMixin, ListView):

    model=Mensajes
    template_name="AppMensajes/mensajeLista.html"

class mensajeDetalle(LoginRequiredMixin, DetailView):

    model=Mensajes
    template_name="AppMensajes/mensajeDetalle.html"

class crearMensaje(LoginRequiredMixin, CreateView):

    model=Mensajes
    success_url="/Mensajes/"
    fields = ['titulo','remitente','recibido', 'mensaje', 'fecha']


class eliminarMensaje(LoginRequiredMixin, DeleteView):

    model=Mensajes
    success_url = "/Mensajes/"
