from django.urls import path, include
from .views import register, meu_perfil

urlpatterns = [
    path('', register, name='signup'),
    path('register/', register, name='register'),
    path('meu-perfil/', meu_perfil, name='meu-perfil'),
]