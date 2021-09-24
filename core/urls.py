from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('wclogon/', include('wclogon.urls'), name='login'),
    path('wcregister/', include('wcregister.urls'), name='register'),
]
