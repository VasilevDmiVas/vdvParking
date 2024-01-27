from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from autopark.forms import CarForm
from autopark.models import CarType


# Create your views here.


def add_car(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            # CarType название модели
            car = CarType()
            car.name = form.cleaned_data['name']
            car.type = form.cleaned_data['type']
            car.save()
            return HttpResponse('Ok')
    else:
        form = CarForm()
    return render(request, 'add_car.html', {'form': form})

