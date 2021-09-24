from django.urls import path, include
from .views import login

urlpatterns = [
    path('', login, name='login'),
    # path('register/', include('wcregister.urls'), name='register'),
]