from django.urls import path
from . import views

urlpatterns = [
    # CRUD
    path('cars/results', views.CarsResults.as_view()),
    path('cars/create', views.CarCreate.as_view()),
    path('cars/<int:pk>', views.CarRetrieveUpdateDestroy.as_view()),

    # Auth
    path('signupuser', views.sign_up_user),
    path('gettoken', views.get_token)
]
