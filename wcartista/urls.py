from django.urls import path, include
from .views import artista, cadastrar

urlpatterns = [
    path('<int:id>', artista, name='artista'),
    path('novo/', cadastrar, name='cadastrar_artista')
]
