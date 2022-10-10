from rest_framework import serializers
from .models import Cifra


class CifraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cifra
        fields = '__all__'
