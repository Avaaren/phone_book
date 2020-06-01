from rest_framework import serializers

from .models import (
    Weather,
    City
)

class WeatherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Weather
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = City
        fields = ('name',)