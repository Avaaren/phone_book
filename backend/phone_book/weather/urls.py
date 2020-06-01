from django.urls import path
from . import views
urlpatterns = [
    path('', views.DisplayWeatherView.as_view()),
    path('add_city/', views.AddCityView.as_view()),
    # path('delete_city/', views.DeleteCityView.as_view()),
]
