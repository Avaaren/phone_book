# Generated by Django 3.0.6 on 2020-06-01 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20200531_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumber',
            name='type_of_number',
            field=models.CharField(choices=[('Мобильный', 'Мобильный'), ('Домашний', 'Домашний')], max_length=35, verbose_name='Тип телефона'),
        ),
    ]