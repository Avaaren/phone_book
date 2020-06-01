from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView
)
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
    '''Отображение и создание пользователя'''
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request):
        '''Отображение списка всех пользователей'''
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request):
        '''Создание нового пользователя с одним или несколькими телефонами'''
        serializer = PersonSerializer(data=request.data)
        
        if serializer.is_valid():
            person = serializer.save()
            serializer = PersonSerializer(person)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PersonEditView(RetrieveUpdateDestroyAPIView):
    '''Редактирование и удаление абонента'''
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_object(self):
        pk = self.kwargs.get('person_id')
        return get_object_or_404(Person, pk=pk)


class PersonAddNumberView(ListCreateAPIView):
    '''Добавление номера для абонента'''
    serializer_class = PhoneNumberSerializer

    def get_queryset(self):
        person_id = self.kwargs.get('person_id')
        owner = get_object_or_404(Person, pk=self.kwargs.get('person_id'))
        return PhoneNumber.objects.filter(owner=owner)

    def perform_create(self, serializer):
        owner = get_object_or_404(Person, pk=self.kwargs.get('person_id'))
        return serializer.save(owner=owner)


class NumberEditView(RetrieveUpdateDestroyAPIView):
    '''Редактирование и удаление номера телефона'''
    serializer_class = PhoneNumberSerializer

    def get_object(self):
        person_pk = self.kwargs.get('person_id')
        number_pk = self.kwargs.get('number_id')

        owner = get_object_or_404(Person, pk=person_pk)
        number = get_object_or_404(PhoneNumber, pk=person_pk, owner=owner)
        return number