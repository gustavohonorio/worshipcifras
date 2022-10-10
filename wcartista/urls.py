from django.urls import path
from .views import artista, cadastrar, ArtistaAPI
from rest_framework.routers import SimpleRouter

# DRF
router_artistas = SimpleRouter()
router_artistas.register('artistas', ArtistaAPI)

urlpatterns = [
    path('<int:id>/<nome_artista>', artista, name='artista'),
    path('novo/', cadastrar, name='cadastrar_artista'),

]
