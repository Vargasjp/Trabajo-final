from django.urls import path
from AppMensajes.views import *

urlpatterns = [
    path('buscaryverMensaje', buscar_verMensaje, name='BuscarVerMensaje'),
    path('mensajeVer/<int:id_mensaje>', mensajeVer, name='MensajeVer'),
    path('mensajeCrear/<username>', mensajeCrear, name='MensajeCrear'),
]