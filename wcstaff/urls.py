from django.urls import path
from .views import staff, artistas, usuarios, cifras

urlpatterns = [
    path('', staff, name='staff'),
    path('artistas/', artistas, name='s-artistas'),
    path('cifras/', cifras, name='s-cifras'),
    path('usuarios/', usuarios, name='s-usuarios'),

]
