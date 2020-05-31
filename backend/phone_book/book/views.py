from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import (
    PersonSerializer,
    PhoneNumberSerializer
)

from .models import (
    Person,
    PhoneNumber
)


class PersonView(APIView):

    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
