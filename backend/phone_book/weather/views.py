from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Weather, City
from .serializers import WeatherSerializer, CitySerializer

from .utils import make_request, create_or_update_weather
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

