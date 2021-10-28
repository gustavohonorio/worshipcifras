from django.urls import path, include
from .views import cifras, cadastrar

urlpatterns = [
    path('', cifras, name='cifras'),
    path('novo/', cadastrar, name='cadastrar_cifra')
]
