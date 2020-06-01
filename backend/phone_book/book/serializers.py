from rest_framework import serializers

from .models import (
    Person,
    PhoneNumber
)
class PhoneNumberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PhoneNumber
        fields = ('id', 'number', 'type_of_number')


class PersonSerializer(serializers.ModelSerializer):
    phones = PhoneNumberSerializer(many=True)
    class Meta:
        model = Person
        fields = '__all__'

    def create(self, validated_data):
        phone_validated_data = validated_data.pop('phones')
        person = Person.objects.create(**validated_data)
        phone_set_serializer = self.fields['phones']
        for phone in phone_validated_data:
            phone['owner'] = person
        phones = phone_set_serializer.create(phone_validated_data)
        return person

