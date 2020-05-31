from django.db import models


class Person(models.Model):
    name = models.CharField('Имя абонента', max_length=35)
    surname = models.CharField('Фамилия абонента', max_length=35)
    patronymic_name = models.CharField('Отчество абонента', max_length=35)
    address = models.CharField('Адрес', max_length=70)
    city = models.CharField('Город', max_length=50)

    def __str__(self):
        return f"{self.name} {self.surname} {self.patronymic_name}"

    class Meta:
        verbose_name = 'Абонент'
        verbose_name_plural = 'Абоненты'


class PhoneNumber(models.Model):
    PHONE_TYPES = (
        ('Мобильный', 'МОБИЛЬНЫЙ'),
        ('Домашний', 'ДОМАШНИЙ'),
    )

    number = models.CharField('Номер телефона', max_length=35)
    type_of_number = models.CharField('Тип телефона', max_length=35, choices=PHONE_TYPES)
    owner = models.ForeignKey(Person, related_name='phones', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.number} - {self.owner}"

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'