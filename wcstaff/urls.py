from django.contrib.auth.decorators import login_required
from django.urls import path
from wcstaff.views import ArtistaListView, CifrasListView, CifrasPendentesListView, UsuariosListView, e_cifras, e_artistas, e_usuarios, usuarios, staff

urlpatterns = [
    path('', staff, name='staff'),

    path('artistas/', login_required(ArtistaListView.as_view()), name='r-artistas'),
    path('artistas/<int:id>', e_artistas, name='e-artistas'),

    path('cifras/', login_required(CifrasListView.as_view()), name='r-cifras'),
    path('cifras/to-approve', login_required(CifrasPendentesListView.as_view()), name='r-cifras-pendentes'),
    path('cifras/<int:id>', e_cifras, name='e-cifras'),

    path('usuarios/', login_required(UsuariosListView.as_view()), name='r-usuarios'),
    path('usuarios/<int:id>', e_usuarios, name='e-usuarios'),


]
