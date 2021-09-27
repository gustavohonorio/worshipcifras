from django.urls import path, include
from .views import artista

urlpatterns = [
    path('', artista, name='artista'),
]
