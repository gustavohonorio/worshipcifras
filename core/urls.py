from django.urls import path, include
from .views import index, CardAPI
from rest_framework.routers import SimpleRouter

# DRF
router_core = SimpleRouter()
router_core.register('card', CardAPI)

urlpatterns = [
    path('', index, name='index'),
    path('logon/', include('wclogon.urls')),
]
