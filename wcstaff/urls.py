from django.urls import path
from wcstaff import views

urlpatterns = [
    path('', views.staff, name='staff'),
    path('artistas/', views.artistas, name='s-artistas'),
    path('artistas/<int:id>', views.e_artistas, name='e-artistas'),

    path('cifras/', views.cifras, name='s-cifras'),
    path('cifras/<int:id>', views.e_cifras, name='e-cifras'),

    path('usuarios/', views.usuarios, name='s-usuarios'),


]
