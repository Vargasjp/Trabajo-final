from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from AppMensajes.forms import MensajesForm, BuscarMensajesForm
from AppMensajes.models import Mensajes
from django.contrib import messages

# Create your views here.

@login_required()
def mensajeCrear(request, username):
    mensaje = MensajesForm(request.POST)
    usernameOrigen = request.user.username
    if request.method == 'POST':
        if mensaje.is_valid():
            mensaje = Mensajes(
                recibido=usernameOrigen,
                remitente=username,
                mensaje=request.POST.get('mensaje'),
            )
            mensaje.save()
            messages.info(request, 'El mensaje se ha enviado con exito!')
        else:
            messages.info(request, 'El mensaje no se ha enviado con exito!')

    contexto = {
        'enviarformulario': MensajesForm(),
        'recibido': username,
    }
    return render(request, 'AppMensajes/mensajeenviar.html', contexto)

@login_required()
def buscar_verMensaje(request):
    buscar = []
    if request.method == 'POST':
        usuarioLogueado = request.user.username
        usuarioorigen = request.POST.get('remitente')
        usuariodestino= request.POST.get('recibido')
        mensaje = request.POST.get('mensaje')

        buscar = (Mensajes.objects.filter(remitente=usuarioLogueado) | \
                   Mensajes.objects.filter(recibido=usuarioLogueado)) & \
                   Mensajes.objects.filter(mensaje__icontains=mensaje) & \
                   Mensajes.objects.filter(remitente__icontains=usuarioorigen) & \
                   Mensajes.objects.filter(recibido__icontains=usuariodestino)

    contexto = {
        'buscar_mensaje': BuscarMensajesForm(),
        'mensaje': buscar,
    }
    return render(request, 'AppMensajes/mensajebuscarver.html', contexto)

@login_required()
def mensajeVer(request, id_mensaje):
    mensaje = Mensajes.objects.get(id_mensaje=id_mensaje)
    mensaje_form = MensajesForm(initial={
        'remitente': mensaje.remitente,
        'recibido': mensaje.recibido,
        'mensaje': mensaje.mensaje,
        'fecha': mensaje.fecha,
    }
    )
    contexto = {
        'formulariomostrarmensaje': mensaje_form,
        'mensaje': mensaje,
    }

    return render(request, 'AppMensajes/mensajever.html', contexto)
