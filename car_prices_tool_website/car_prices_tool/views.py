from django.shortcuts import render
from django.http import HttpResponse
from car_prices_tool.models import Car
from django.core import serializers
from django.db.models import Count
from car_prices_tool.forms import SearchCarForm


def home(request):
    cars = Car.objects.filter()
    cars_below = Car.objects.filter(mileage__lte=150000)
    cars_below_2 = Car.objects.filter(price__lte=150000)
    context = {
        'cars': cars,
        'cars_below': cars_below,
        'cars_below_2': cars_below_2
    }

    return render(request, 'car_prices_tool/home.html', context)


def search(request):
    cars = Car.objects.all()
    makes = Car.objects.values('make').annotate(entries=Count('make'))
    models = Car.objects.values('model').annotate(entries=Count('model'))

    form = SearchCarForm

    if request.method == 'POST':
        filled_form = SearchCarForm(request.POST)
        if filled_form.is_valid():
            context = {
                'make': filled_form.cleaned_data['make'],
                'state': filled_form.cleaned_data['state'],
                'model': filled_form.cleaned_data['model'],
                'offer_type': filled_form.cleaned_data['offer_type'],
                'mileage_less_more': filled_form.cleaned_data['mileage_less_more'],
                'mileage': filled_form.cleaned_data['mileage'],
                'production_year_less_more': filled_form.cleaned_data['production_year_less_more'],
                'production_year': filled_form.cleaned_data['production_year'],
                'price_less_more': filled_form.cleaned_data['price_less_more'],
                'price': filled_form.cleaned_data['price'],
                'price_currency': filled_form.cleaned_data['price_currency'],
                'engine_capacity_less_more': filled_form.cleaned_data['engine_capacity_less_more'],
                'engine_capacity': filled_form.cleaned_data['engine_capacity'],
                'engine_power_less_more': filled_form.cleaned_data['engine_power_less_more'],
                'engine_power': filled_form.cleaned_data['engine_power']
            }

            return results(request, context)

    context = {
        'cars': cars,
        'makes': makes,
        'models': models,
        'form': form
    }

    return render(request, 'car_prices_tool/search.html', context)


def results(request, context):
    make = context.get('make')
    state = context.get('state')
    model = context.get('model')
    offer_type = context.get('offer_type')
    mileage_less_more = context.get('mileage_less_more')
    mileage = context.get('mileage')
    production_year_less_more = context.get('production_year_less_more')
    production_year = context.get('production_year')
    price_less_more = context.get('price_less_more')
    price = context.get('price')
    price_currency = context.get('price_currency')
    engine_capacity_less_more = context.get('engine_capacity_less_more')
    engine_capacity = context.get('engine_capacity')
    engine_power_less_more = context.get('engine_power_less_more')
    engine_power = context.get('engine_power')

    context = {
        'make': context.get('make'),
        'state': context.get('state')
    }

    return render(request, 'car_prices_tool/results.html', context)
