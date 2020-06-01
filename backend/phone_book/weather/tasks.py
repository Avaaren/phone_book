from celery import shared_task

from .models import Weather
from .utils import make_request, create_or_update_weather

@shared_task
def update_weather_data():

    weather_set = Weather.objects.all()

    for weather in weather_set:
        response = make_request(weather.city_name)

        create_or_update_weather(response=response, statement='update', weather=weather)
