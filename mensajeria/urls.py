from django.urls import path
from . import views

urlpatterns = [
    path('', views.bandeja_entrada, name='bandeja_entrada'),
    path('enviar/', views.enviar_mensaje, name='enviar_mensaje'),
    path('<int:pk>/', views.ver_mensaje, name='ver_mensaje'),
]