from django.urls import path
from .views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("vehiculos/", vehiculosformulario, name="vehiculosFormulario"),
    path("clientes/", clientesformulario, name="clientesFormulario"),
    path("empleados/", empleadosformulario, name="empleadosFormulario"),
    path("busquedaCliente/", busquedaCliente, name="busquedaCliente"),
    path("buscar/", buscar, name="buscar"),
    path("sobreNosotros", sobreNosotros, name="sobreNosotros"),
    path("nuestrosVehiculos", leerVehiculos, name="nuestrosVehiculos"),
]