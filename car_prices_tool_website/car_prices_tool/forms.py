from django import forms
from car_prices_tool.models import Car
from django.db.models import Count


class SearchCarForm(forms.Form):
    make = forms.ModelChoiceField(queryset=Car.objects.values('make').annotate(entries=Count('make')))
    state_choices = [('used', 'Used'), ('new', 'New'), ('both', 'Both')]
    state = forms.ChoiceField(widget=forms.RadioSelect, choices=state_choices)


class OptionalSearchCarForm(forms.Form):
    # Model:
    model = forms.ModelChoiceField(
        queryset=Car.objects.values('model').filter(make='Audi').annotate(entries=Count('model')))

    # Offer type:
    offer_type_choices = [('all', 'All'),
                          ('person', 'Person'),
                          ('company', 'Company')]
    offer_type = forms.ChoiceField(widget=forms.RadioSelect, choices=offer_type_choices)

    # Mileage:
    mileage_less_more_choices = [('mileage_less_than', 'Equal or less than:'),
                                 ('mileage_more_than', 'Equal or more than:')]
    mileage_less_more = forms.ChoiceField(widget=forms.RadioSelect, choices=mileage_less_more_choices)
    mileage = forms.IntegerField()

    # Production year:
    production_year_less_more_choices = [('production_year_less_than', 'Equal or earlier than:'),
                                         ('production_year_more_than', 'Equal or later than:'),
                                         ('production_year_exact', 'Exact:')]
    production_year_less_more = forms.ChoiceField(widget=forms.RadioSelect, choices=production_year_less_more_choices)
    production_year = forms.IntegerField()

    # Price:
    price_less_more_choices = [('price_less_than', 'Equal or less than:'),
                               ('price_more_than', 'Equal or more than:')]
    price_less_more = forms.ChoiceField(widget=forms.RadioSelect, choices=production_year_less_more_choices)
    price = forms.IntegerField()

    # Price currency:
    price_currency_choices = [('pln', 'Currency: PLN'),
                              ('usd', 'Currency: USD'),
                              ('eur', 'Currency: EUR')]
    price_currency = forms.ChoiceField(widget=forms.RadioSelect, choices=price_currency_choices)

    # Engine capacity:
    engine_capacity_choices = [('engine_capacity_less_than', 'Equal or less than:'),
                               ('engine_capacity_more_than', 'Equal or more than:'),
                               ('engine_capacity_equal', 'Exact:')]
    engine_capacity_less_more = forms.ChoiceField(widget=forms.RadioSelect, choices=engine_capacity_choices)
    engine_capacity = forms.IntegerField()

    # Engine power:
    engine_power_choices = [('engine_power_less_than', 'Equal or less than:'),
                            ('engine_power_more_than', 'Equal or more than:'),
                            ('engine_power_equal', 'Exact:')]
    engine_power_less_more = forms.ChoiceField(widget=forms.RadioSelect, choices=engine_power_choices)
    engine_power = forms.IntegerField()
