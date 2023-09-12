from django.urls import path, include
from .views import index, pre_alfa, CardAPI
from rest_framework.routers import SimpleRouter

# DRF
router_core = SimpleRouter()
router_core.register('card', CardAPI)

urlpatterns = [
    path('', pre_alfa, name='index'),  # QUANDO LIBERAR O PRODUTO PARA PRODUÇÃO, BASTA AJUSTAR ESTE DIRECIONAMENTO
    path('dev/', index, name='index2'),
    path('logon/', include('wclogon.urls')),
]
