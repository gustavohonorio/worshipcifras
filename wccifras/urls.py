from django.urls import path, include
from .views import cifras, cadastrar

urlpatterns = [
    path('', cifras, name='cifras'),
    path('busca/<int:cifra_id>/', cifras, name='cifras_busca'),
    path('novo/', cadastrar, name='cadastrar_cifra')
]
