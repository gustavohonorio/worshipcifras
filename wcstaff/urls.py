from django.urls import path
from .views import staff, artistas, e_artistas, usuarios, cifras

urlpatterns = [
    path('', staff, name='staff'),
    path('artistas/', artistas, name='s-artistas'),
    path('artistas/<int:id>', e_artistas, name='e-artistas'),

    path('cifras/', cifras, name='s-cifras'),

    path('usuarios/', usuarios, name='s-usuarios'),


]
