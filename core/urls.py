from django.urls import path, include
from .views import index, pre_alfa

urlpatterns = [
    # path('', index, name='index'),
    path('', pre_alfa, ),  # landing page
    path('acesso/', index, name='index'),
    path('logon/', include('wclogon.urls')),
]
