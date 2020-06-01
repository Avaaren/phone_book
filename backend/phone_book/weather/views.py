from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Weather
from .serializers import WeatherSerializer
import requests


class DisplayWeatherView(APIView):

    def get(self, request):
        city = 'Minsk'
        api_key = '8511d8d7ec587c22c41790a2b95f0247'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'

        response = requests.get(url).json()
        city_name = response.get('name')
        temperature = response['main'].get('temp')
        wind_speed = response['wind'].get('speed')
        weather_condition = response['weather'][0].get('description')
        weather_icon_id = response['weather'][0].get('icon')
        s=Weather.objects.filter(city_name=city_name)
        if s:
            s.update(
                temperature = temperature,
                wind_speed = wind_speed,
                weather_condition = weather_condition,
                weather_icon_id = weather_icon_id,
            )
        else:
             Weather.objects.create(
                city_name=city_name,
                temperature = temperature,
                wind_speed = wind_speed,
                weather_condition = weather_condition,
                weather_icon_id = weather_icon_id,
            )
        queryset = Weather.objects.all()
        serializer = WeatherSerializer(queryset, many=True)
        return Response(serializer.data)

