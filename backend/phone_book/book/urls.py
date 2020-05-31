from django.urls import path

from . import views

urlpatterns = [
    path('', views.PersonView.as_view())
]