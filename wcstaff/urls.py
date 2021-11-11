from django.urls import path
from .views import staff

urlpatterns = [
    path('', staff, name='staff'),

]
