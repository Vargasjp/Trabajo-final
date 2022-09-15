from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name="inicio"),
    path("vehiculos/", vehiculosformulario, name="vehiculosFormulario"),
    path("clientes/", clientesformulario, name="clientesFormulario"),
    path("empleados/", empleadosformulario, name="empleadosFormulario"),
    path("busquedaCliente/", busquedaCliente, name="busquedaCliente"),
    path("buscar/", buscar, name="buscar"),
    path("sobreNosotros", sobreNosotros, name="sobreNosotros"),
    path("nuestrosVehiculos", leerVehiculos, name="nuestrosVehiculos"),
    path("login/", login_request, name="login"),
    path("register/", register, name="register"),
    path("logout/", LogoutView.as_view(template_name="AppConcesionaria/logout.html"), name="logout"),
    path("editarPerfil/", editarPerfil, name="editarPerfil"),
    path("verMas/<id>", verMas, name="verMas"),
]