from django.urls import path
from AppMensajes.views import *

urlpatterns = [
    path('', mensajeLista.as_view(), name="Mensajes"),
    path('nuevoMensaje/', crearMensaje.as_view(), name="crearMensaje"),
    path('<pk>/', mensajeDetalle.as_view(), name="detalleMensaje"),
    path("eliminar/<pk>", eliminarMensaje.as_view(), name="eliminarMensaje"),
]