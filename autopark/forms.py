from django import forms

from autopark.models import CarType


class CarForm(forms.Form):
    name = forms.CharField(max_length=100, label='Введите марку авто')


class Car_all(forms.Form):
    car_number = forms.CharField(max_length=10, label='Введите гос номер авто')
    year = forms.IntegerField(label='Введите год выпуска авто')
    name = forms.CharField(max_length=100, label='Введите тип авто')
    # car_type = forms.ModelChoiceField(queryset=CarType.objects.all(), label='Выберите тип авто')
    is_electric = forms.BooleanField(label='Электропривод', required=False)

