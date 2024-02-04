from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from autopark.forms import CarForm, Car_all, CarTypeForm
from autopark.models import CarBrand, Car, CarType


# Create your views here.


def add_carBrand(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            # CarBrand название модели
            car = CarBrand()
            car.name = form.cleaned_data['name']
            car.save()
            return HttpResponse('Ok')
    else:
        form = CarForm()
    return render(request, 'add_carBrand.html', {'form': form})


def add_carType(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CarTypeForm(request.POST)
        if form.is_valid():
            # CarType название модели
            car_type = CarType()
            car_type.name = form.cleaned_data['name']
            car_type.save()
            return HttpResponse('Ok')
    else:
        form = CarTypeForm()
    return render(request, 'add_carType.html', {'form': form})


def add_car_all(request):
    car_list = CarBrand.objects.all()
    car_form = Car_all()
    if request.method == 'POST':
        car_form = Car_all(request.POST)
        car_type = request.POST.getlist('car_type')
        if car_form.is_valid():
            car_form = Car(
                car_number=car_form.cleaned_data['car_number'],
                year=car_form.cleaned_data['year'],
                is_electric=car_form.cleaned_data['is_electric'],
                car_brand=CarBrand.objects.get(id=car_type[0]),
            )
            car_form.save()
            # CarType название модели
            # нет доступа к таблице CarBrand
            car_form.save()
            return HttpResponse('Ok')
    data = {
        'car_type': car_list,
        'form': car_form
    }
    return render(request, 'add_car_all.html', context=data)
