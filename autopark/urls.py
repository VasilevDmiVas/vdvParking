from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.add_car, name='add_car'),
    path('add_car_all', views.add_car_all, name='add_car_all'),

]
