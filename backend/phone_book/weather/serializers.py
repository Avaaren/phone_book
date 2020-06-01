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

    def create(self, validated_data):
        city_name = validated_data.get('name')

        obj, created = City.objects.get_or_create(name=city_name)

        return obj
        