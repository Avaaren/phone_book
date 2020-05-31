from django.urls import path

from . import views

urlpatterns = [
    path('', views.PersonListView.as_view()),
    path('<int:person_id>', views.PersonEditView.as_view()),
    path('<int:person_id>/<int:number_id>/', views.NumberEditView.as_view()),
]