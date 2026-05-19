from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.VistaRegistro.as_view(), name='registro'),
    path('login/', views.vista_login, name='login'),
    path('logout/', views.vista_logout, name='logout'),
    path('perfil/', views.VistaPerfil.as_view(), name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/password/', views.cambiar_password, name='cambiar_password'),
]