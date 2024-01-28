from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from autopark.forms import CarForm, Car_all
from autopark.models import CarBrand, Car


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


def add_car_all(request):
    car_list = CarBrand.objects.all()
    car_form = Car_all()
    if request.method == 'POST':
        car_form = Car_all(request.POST)
        users = request.POST.getlist('users')
        if car_form.is_valid():
            car_form = Car(
                car_number=car_form.cleaned_data['car_number'],
                year=car_form.cleaned_data['year'],
            )
            car_form.save()
            # CarType название модели
            # нет доступа к таблице CarBrand
            car_form.save()
            return HttpResponse('Ok')
    data = {
        'users': car_list,
        'form': car_form
    }
    return render(request, 'add_car_all.html', context=data)