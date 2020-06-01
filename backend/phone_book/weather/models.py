from django.db import models


class City(models.Model):
    name = models.CharField('Город', max_length=50)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class Weather(models.Model):
    city_name = models.CharField('Название города', max_length=50)
    temperature = models.FloatField('Температура', default=0)
    wind_speed = models.FloatField('Скорость ветра', default=0)
    weather_condition = models.CharField('Погода', max_length=50)
    weather_icon_id = models.CharField('Иконка погоды', max_length=5)
    time = models.DateTimeField('Вермя последнего обновления', auto_now=True)

    class Meta:
        verbose_name = 'Информация о погоде'
        verbose_name_plural = 'Информация о погоде'

    def __str__(self):
        return f'{self.city_name}-{self.time}'

