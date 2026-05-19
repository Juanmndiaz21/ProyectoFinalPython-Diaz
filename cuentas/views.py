from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import (
    FormularioRegistro,
    FormularioEditarUsuario,
    FormularioEditarPerfil,
    FormularioCambiarPassword,
)
from .models import Perfil


# CBV #1 — Registro
class VistaRegistro(View):
    def get(self, request):
        formulario = FormularioRegistro()
        return render(request, 'cuentas/registro.html', {'formulario': formulario})

    def post(self, request):
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            Perfil.objects.create(usuario=usuario)
            login(request, usuario)
            messages.success(request, '¡Cuenta creada exitosamente!')
            return redirect('inicio')
        return render(request, 'cuentas/registro.html', {'formulario': formulario})


# CBV #2 — Ver perfil (con LoginRequiredMixin = mixin)
class VistaPerfil(LoginRequiredMixin, View):
    def get(self, request):
        perfil, creado = Perfil.objects.get_or_create(usuario=request.user)
        return render(request, 'cuentas/perfil.html', {'perfil': perfil})


# Decorador — Login
def vista_login(request):
    if request.method == 'POST':
        nombre_usuario = request.POST.get('username')
        contrasena = request.POST.get('password')
        usuario = authenticate(request, username=nombre_usuario, password=contrasena)
        if usuario:
            login(request, usuario)
            return redirect('inicio')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'cuentas/login.html')


def vista_logout(request):
    logout(request)
    return redirect('inicio')


# Decorador obligatorio de la rúbrica
@login_required
def editar_perfil(request):
    perfil, creado = Perfil.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        form_usuario = FormularioEditarUsuario(request.POST, instance=request.user)
        form_perfil = FormularioEditarPerfil(request.POST, request.FILES, instance=perfil)

        if form_usuario.is_valid() and form_perfil.is_valid():
            form_usuario.save()
            form_perfil.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('perfil')
    else:
        form_usuario = FormularioEditarUsuario(instance=request.user)
        form_perfil = FormularioEditarPerfil(instance=perfil)

    return render(request, 'cuentas/editar_perfil.html', {
        'form_usuario': form_usuario,
        'form_perfil': form_perfil,
    })


@login_required
def cambiar_password(request):
    if request.method == 'POST':
        formulario = FormularioCambiarPassword(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            usuario = authenticate(
                request,
                username=request.user.username,
                password=datos['password_actual']
            )
            if usuario:
                usuario.set_password(datos['password_nuevo'])
                usuario.save()
                update_session_auth_hash(request, usuario)
                messages.success(request, 'Contraseña cambiada correctamente.')
                return redirect('perfil')
            else:
                messages.error(request, 'La contraseña actual es incorrecta.')
    else:
        formulario = FormularioCambiarPassword()

    return render(request, 'cuentas/cambiar_password.html', {'formulario': formulario})