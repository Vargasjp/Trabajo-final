from django.urls import path
from AppMensajes.views import *

urlpatterns = [
    path('', MensajeLista.as_view(), name="mensajeLista"),
    path('nuevo/', CrearMensaje.as_view(), name="nuevoMensaje"),
    path('<pk>/', MensajeDetalle.as_view(), name="detalleMensaje"),
    path('eliminar/<pk>', EliminarMensaje.as_view(), name="eliminarMensaje"),
]