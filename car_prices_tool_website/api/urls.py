from django.urls import path
from . import views

urlpatterns = [
    path('cars/results', views.CarsResults.as_view()),
    path('cars/create', views.CarCreate.as_view())
]
