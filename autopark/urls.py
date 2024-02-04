from django.urls import path, include
from . import views

urlpatterns = [
    path('add_carBrand', views.add_carBrand, name='add_carBrand'),
    path('add_carType', views.add_carType, name='add_carType'),
    path('add_car_all', views.add_car_all, name='add_car_all'),

]
