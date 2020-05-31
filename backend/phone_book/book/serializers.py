from rest_framework import serializers

from .models import (
    Person,
    PhoneNumber
)
class PhoneNumberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PhoneNumber
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    phones = PhoneNumberSerializer(many=True)
    class Meta:
        model = Person
        fields = '__all__'

