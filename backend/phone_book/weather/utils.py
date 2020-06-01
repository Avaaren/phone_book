import requests
from .models import Weather

def make_request(city):
    api_key = '8511d8d7ec587c22c41790a2b95f0247'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
    response = requests.get(url).json()
    return response

def create_or_update_weather(response, statement, weather=None):

    city_name = response.get('name')
    temperature = response['main'].get('temp')
    wind_speed = response['wind'].get('speed')
    weather_condition = response['weather'][0].get('description')
    weather_icon_id = response['weather'][0].get('icon')

    if statement == 'update':
        weather.temperature=temperature
        weather.wind_speed=wind_speed
        weather.weather_condition=weather_condition
        weather.weather_icon_id=weather_icon_id

        weather.save()
        
    if statement == 'create':

        Weather.objects.get_or_create(
                city_name=city_name,
                temperature = temperature,
                wind_speed = wind_speed,
                weather_condition = weather_condition,
                weather_icon_id = weather_icon_id,
            )

