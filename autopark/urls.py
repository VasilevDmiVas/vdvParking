from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.add_car, name='add_car'),

]
