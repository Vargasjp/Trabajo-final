from django.urls import path
from AppMensajeria.views import *

urlpatterns = [
    path("crearMensaje/", crearMensaje, name="crearMensaje"),
    path("leerMensajes/", leerMensajes, name="leerMensajes"),
    path("verMensaje/<id>", verMensaje, name="verMensaje"),
]