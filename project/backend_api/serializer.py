from rest_framework import serializers
from .models import main

class mainSerializer(serializers.ModelSerializer):
    class Meta:
        model = main
        fields = ['title', 'description']