from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Mensaje
from .forms import FormularioMensaje


@login_required
def bandeja_entrada(request):
    mensajes_recibidos = Mensaje.objects.filter(destinatario=request.user)
    return render(request, 'mensajeria/bandeja.html', {'mensajes_recibidos': mensajes_recibidos})


@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        formulario = FormularioMensaje(request.POST)
        if formulario.is_valid():
            mensaje = formulario.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            messages.success(request, 'Mensaje enviado correctamente.')
            return redirect('bandeja_entrada')
    else:
        formulario = FormularioMensaje()
    return render(request, 'mensajeria/enviar.html', {'formulario': formulario})


@login_required
def ver_mensaje(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)
    if mensaje.destinatario == request.user and not mensaje.leido:
        mensaje.leido = True
        mensaje.save()
    return render(request, 'mensajeria/ver_mensaje.html', {'mensaje': mensaje})