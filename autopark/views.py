from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from autopark.forms import CarForm, Car_all
from autopark.models import CarType, Car


# Create your views here.


def add_car(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            # CarType название модели
            car = CarType()
            car.name = form.cleaned_data['name']
            car.save()
            return HttpResponse('Ok')
    else:
        form = CarForm()
    return render(request, 'add_car.html', {'form': form})


def add_car_all(request: HttpRequest) -> HttpResponse:
    car_list = CarType.objects.all()
    car_form = Car_all()
    if request.method == 'POST':
        car_form = Car_all(request.POST)
        if car_form.is_valid():
            car_form = Car(
                car_number=car_form.cleaned_data['car_number'],
                year=car_form.cleaned_data['year'],

            )
            car_form.save()
            car_form.car_type_id = car_form.id
            car_form.save()



            # CarType название модели
            return HttpResponse('Ok')
    data = {
        'users': car_list,
        'form': car_form
    }
    return render(request, 'add_car_all.html', context=data)