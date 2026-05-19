from django.urls import path
from . import views

urlpatterns = [
    path('', views.VistaInicio.as_view(), name='inicio'),
    path('about/', views.VistaAcercaDe.as_view(), name='acerca_de'),
    path('pages/', views.VistaListaPaginas.as_view(), name='lista_paginas'),
    path('pages/<int:pk>/', views.detalle_pagina, name='detalle_pagina'),
    path('pages/crear/', views.crear_pagina, name='crear_pagina'),
    path('pages/<int:pk>/editar/', views.editar_pagina, name='editar_pagina'),
    path('pages/<int:pk>/borrar/', views.borrar_pagina, name='borrar_pagina'),
]