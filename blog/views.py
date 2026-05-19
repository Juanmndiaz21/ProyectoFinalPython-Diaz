from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages

from .models import Pagina
from .forms import FormularioPagina


# Vista inicio — CBV
class VistaInicio(View):
    def get(self, request):
        return render(request, 'blog/inicio.html')


# Vista about
class VistaAcercaDe(View):
    def get(self, request):
        return render(request, 'blog/acerca_de.html')


# Vista listado de páginas — CBV
class VistaListaPaginas(View):
    def get(self, request):
        paginas = Pagina.objects.all()
        return render(request, 'blog/lista_paginas.html', {'paginas': paginas})


# Vista detalle — función simple
def detalle_pagina(request, pk):
    pagina = get_object_or_404(Pagina, pk=pk)
    return render(request, 'blog/detalle_pagina.html', {'pagina': pagina})


# Crear — requiere login (decorador)
@login_required
def crear_pagina(request):
    if request.method == 'POST':
        formulario = FormularioPagina(request.POST, request.FILES)
        if formulario.is_valid():
            pagina = formulario.save(commit=False)
            pagina.autor = request.user
            pagina.save()
            messages.success(request, 'Página creada correctamente.')
            return redirect('lista_paginas')
    else:
        formulario = FormularioPagina()
    return render(request, 'blog/formulario_pagina.html', {
        'formulario': formulario,
        'accion': 'Crear'
    })


# Editar — requiere login (decorador)
@login_required
def editar_pagina(request, pk):
    pagina = get_object_or_404(Pagina, pk=pk)
    if request.method == 'POST':
        formulario = FormularioPagina(request.POST, request.FILES, instance=pagina)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Página actualizada correctamente.')
            return redirect('lista_paginas')
    else:
        formulario = FormularioPagina(instance=pagina)
    return render(request, 'blog/formulario_pagina.html', {
        'formulario': formulario,
        'accion': 'Editar'
    })


# Borrar — requiere login (decorador)
@login_required
def borrar_pagina(request, pk):
    pagina = get_object_or_404(Pagina, pk=pk)
    if request.method == 'POST':
        pagina.delete()
        messages.success(request, 'Página eliminada correctamente.')
        return redirect('lista_paginas')
    return render(request, 'blog/confirmar_borrado.html', {'pagina': pagina})