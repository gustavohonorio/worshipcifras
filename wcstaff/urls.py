from django.urls import path
from wcstaff import views

urlpatterns = [
    path('', views.staff, name='staff'),

    path('artistas/', views.artistas, name='r-artistas'),
    path('artistas/<int:id>', views.e_artistas, name='e-artistas'),

    path('cifras/visualizar/<filtro>', views.cifras, name='r-cifras'),
    path('cifras/<int:id>', views.e_cifras, name='e-cifras'),

    path('usuarios/', views.usuarios, name='r-usuarios'),
    path('usuarios/<int:id>', views.e_usuarios, name='e-usuarios'),


]
