from django.http import HttpResponse
from django.shortcuts import render

from AppConcesionaria.forms import *
from .models import Vehiculos, Clientes, Empleados
# Create your views here.

def inicio(request):
    return render(request, "AppConcesionaria/inicio.html")

def vehiculosformulario(request):
    if request.method=="POST":
        miFormulario=VehiculoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            marca=info.get("marca")
            tipo=info.get("tipo")
            color=info.get("color")
            kilometros=info.get("kilometros")
            vehiculo=Vehiculos(marca=marca, tipo=tipo, color=color, kilometros=kilometros)
            vehiculo.save()
            return render(request, "AppConcesionaria/inicio.html", {"mensaje": "Vehiculo Agregado"})
        else:
            return render(request, "AppConcesionaria/inicio.html", {"mensaje": "Error"})
    else:
        miFormulario=VehiculoFormulario()
        return render(request, "AppConcesionaria/accesoVehiculos.html", {"formulario":miFormulario})

def clientesformulario(request):
    if request.method=="POST":
        miFormulario=ClienteForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            nombre=info.get("nombre")
            apellido=info.get("apellido")
            email=info.get("email")
            dni=info.get("dni")
            cliente=Clientes(nombre=nombre, apellido=apellido, email=email, dni=dni)
            cliente.save()
            return render(request, "AppConcesionaria/inicio.html", {"mensaje": "Cliente Agregado"})
        else:
            return render(request, "AppConcesionaria/inicio.html", {"mensaje": "Error"})
    else:
        miFormulario=ClienteForm()
        return render(request, "AppConcesionaria/accesoClientes.html", {"formulario":miFormulario})

def empleadosformulario(request):
    if request.method=="POST":
        miFormulario=EmpleadoForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            nombre=info.get("nombre")
            apellido=info.get("apellido")
            dni=info.get("dni")
            email=info.get("email")
            cargo=info.get("cargo")
            empleado=Empleados(nombre=nombre, apellido=apellido, dni=dni, email=email, cargo=cargo)
            empleado.save()
            return render(request, "AppConcesionaria/inicio.html", {"mensaje": "Empleado Agregado"})
        else:
            return render(request, "AppConcesionaria/inicio.html", {"mensaje": "Error"})
    else:
        miFormulario=EmpleadoForm()
        return render(request, "AppConcesionaria/accesoEmpleados.html", {"formulario":miFormulario})


def busquedaCliente(request):
    return render(request, "AppConcesionaria/busquedaCliente.html")

def buscar(request):
    if request.GET["dni"]:
        dni=request.GET["dni"]
        DNI=Clientes.objects.filter(dni=dni)
        if len(DNI)!=0:
            return render(request, "AppConcesionaria/ResultadoBusqueda.html", {"cliente":DNI})
        else:
            return render(request, "AppConcesionaria/ResultadoBusqueda.html", {"mensaje": "No hay clientes con ese DNI"})
    else:
        return render(request, "AppConcesionaria/busquedaCliente.html", {"mensaje": "No enviaste datos!"})

def sobreNosotros(request):
    return render(request, "AppConcesionaria/sobreNosotros.html")

def leerVehiculos(request):
    vehiculos=Vehiculos.objects.all()
    contexto={"vehiculos":vehiculos}
    return render(request, "AppConcesionaria/nuestrosVehiculos.html", contexto)