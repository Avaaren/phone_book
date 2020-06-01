from django.contrib import admin

from .models import Weather, City

@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    
    class Meta:
        list_display = '__all__'

        
@admin.register(City)
class WeatherAdmin(admin.ModelAdmin):
    class Meta:
        list_display = '__all__'
