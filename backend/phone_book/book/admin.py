from django.contrib import admin

from .models import (
    Person,
    PhoneNumber
)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    
    class Meta:
        list_display = '__all__'

@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    
    class Meta:
        list_display = '__all__'
