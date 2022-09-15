from django.http import HttpResponse
from django.shortcuts import render

from AppConcesionaria.forms import *
from .models import Vehiculos, Clientes, Empleados
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
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
            imagen=info.get("imagen")
            fechaDePublicacion=info.get("fechaDePublicacion")
            vehiculo=Vehiculos(marca=marca, tipo=tipo, color=color, kilometros=kilometros, imagen=imagen, fechaDePublicacion=fechaDePublicacion)
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

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password")
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppConcesionaria/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppConcesionaria/login.html", {"form":form,"mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "AppConcesionaria/login.html", {"form":form,"mensaje":"Formulario Invalido"})
    else:
        form=AuthenticationForm()
        return render(request, "AppConcesionaria/login.html", {"form":form})

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            return render(request, "AppConcesionaria/inicio.html", {"mensaje":f"Usuario: {username} creado"})
    else:
        form=UserRegisterForm()
    return render(request,"AppConcesionaria/register.html", {"form":form})

@login_required
def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditform(request.POST, instance=usuario)
        if form.is_valid():
            usuario.first_name=form.cleaned_data["first_name"]
            usuario.last_name=form.cleaned_data["last_name"]
            usuario.email=form.cleaned_data["email"]
            usuario.save()
            return render(request, "AppConcesionaria/inicio.html", {"mensaje":f"Perfil de {usuario} editado"})
    else:
        form=UserEditform(instance=usuario)
        return render(request, "AppConcesionaria/editarPerfil.html", {"form":form, "usuario":usuario})

def verMas(request,id):
    vehi=Vehiculos.objects.get(id=id)
    contexto={"vehiculo":vehi}
    return render(request, "AppConcesionaria/verMas.html", contexto)
    