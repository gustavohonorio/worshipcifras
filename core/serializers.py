from rest_framework import serializers
from .models import CardDestaque


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardDestaque
        fields = '__all__'
