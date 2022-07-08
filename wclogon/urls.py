from django.urls import path, include
from .views import register, meu_perfil, redefinir_senha, esqueci_senha

urlpatterns = [
    path('', register, name='signup'),
    path('register/', register, name='register'),
    path('recuperar-senha/', esqueci_senha, name='esqueci-senha'),
    path('meu-perfil/dados-pessoais/', meu_perfil, name='meu-perfil'),
    path('meu-perfil/redefinir-senha/', redefinir_senha, name='redefinir-senha'),
]