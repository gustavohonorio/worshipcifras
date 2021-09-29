from django.urls import path, include
from .views import cifras

urlpatterns = [
    path('', cifras, name='cifras'),
]
