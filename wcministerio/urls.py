from django.urls import path
from .views import MinisteriosView

urlpatterns = [
    path('', MinisteriosView.as_view(), name='ministerio'),
]