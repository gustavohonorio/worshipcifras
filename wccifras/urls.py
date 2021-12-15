from django.urls import path, include
from .views import cifras, cadastrar

urlpatterns = [
    path('', cifras, name='cifras'),
    path('<artista>/<int:cifra_id>/<cifra_nome>/<modo_v>', cifras, name='cifras_busca'),
    path('novo/', cadastrar, name='cadastrar_cifra')
]
