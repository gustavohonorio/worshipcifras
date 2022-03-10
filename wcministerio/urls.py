from django.urls import path
from .views import ministerios

urlpatterns = [
    path('', ministerios, name='ministerio'),

]