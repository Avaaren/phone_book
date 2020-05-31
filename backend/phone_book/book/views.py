from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import (
    PersonSerializer,
    PhoneNumberSerializer
)

from .models import (
    Person,
    PhoneNumber
)


class PersonListView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)


class PersonEditView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_object(self):
        pk = self.kwargs.get('person_id')
        return get_object_or_404(Person, pk=pk)


class NumberEditView(RetrieveUpdateDestroyAPIView):
    # queryset = Person.objects.all()
    serializer_class = PhoneNumberSerializer

    def get_object(self):
        person_pk = self.kwargs.get('person_id')
        number_pk = self.kwargs.get('number_id')
        try:
            number = Person.objects.get(pk=person_pk).phones.get(pk=number_pk)
        except PhoneNumber.DoesNotExist:
            raise Http404('Lol')
        return number