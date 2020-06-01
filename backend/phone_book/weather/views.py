from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Weather, City
from .serializers import WeatherSerializer, CitySerializer

from .utils import make_request, create_or_update_weather
from .tasks import update_weather_data
import requests


class DisplayWeatherView(ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer


class AddCityView(ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    
    def perform_create(self, serializer):
        response = make_request(serializer.validated_data.get("name"))

        create_or_update_weather(response=response, statement='create')
        return serializer.save()

class DeleteCityView(RetrieveUpdateDestroyAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()

