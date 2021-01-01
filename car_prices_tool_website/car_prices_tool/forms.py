from django import forms
from car_prices_tool.models import Car, CarMake


class SearchCarForm(forms.Form):
    make_choices = []
    makes = CarMake.objects.values('car_make')
    # for make in makes:
    #     make_choices.append((make["car_make"], f'{make["car_make"]} ({CarMake.objects.filter(make=make["car_make"]).count()})'))
    for make in makes:
        make_choices.append((make["car_make"], f'{make["car_make"]}'))
    make = forms.ChoiceField(choices=make_choices)
    state_choices = [('used', 'Used'), ('new', 'New'), ('both', 'Both')]
    state = forms.ChoiceField(widget=forms.RadioSelect, choices=state_choices)

    # Model:
    # model_choices = []
    # models = Car.objects.values('model').distinct()
    # for model in models:
    #     model_choices.append((model["model"], f'{model["model"]} ({Car.objects.filter(model=model["model"]).count()})'))
    # model = forms.ChoiceField(choices=model_choices)

    model = forms.ChoiceField()

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['model'].queryset = CarMake.objects.none()

    # Offer type:
    offer_type_choices = [('all', 'All'),
                          ('person', 'Person'),
                          ('company', 'Company')]
    offer_type = forms.ChoiceField(widget=forms.RadioSelect, choices=offer_type_choices, required=False)

    # Mileage:
    mileage_less_more_choices = [('mileage_less_than', 'Equal or less than:'),
                                 ('mileage_more_than', 'Equal or more than:')]
    mileage_less_more = forms.ChoiceField(widget=forms.RadioSelect, choices=mileage_less_more_choices, required=False)
    mileage = forms.IntegerField(required=False)

    # Production year:
    production_year_less_more_choices = [('production_year_less_than', 'Equal or earlier than:'),
                                         ('production_year_more_than', 'Equal or later than:'),
                                         ('production_year_exact', 'Exact:')]
    production_year_less_more = forms.ChoiceField(widget=forms.RadioSelect, choices=production_year_less_more_choices, required=False)
    production_year = forms.IntegerField(required=False)

    # Price:
    price_less_more_choices = [('price_less_than', 'Equal or less than:'),
                               ('price_more_than', 'Equal or more than:')]
    price_less_more = forms.ChoiceField(widget=forms.RadioSelect, choices=production_year_less_more_choices, required=False)
    price = forms.IntegerField(required=False)

    # Price currency:
    price_currency_choices = [('pln', 'Currency: PLN'),
                              ('usd', 'Currency: USD'),
                              ('eur', 'Currency: EUR')]
    price_currency = forms.ChoiceField(widget=forms.RadioSelect, choices=price_currency_choices, required=False)

    # Engine capacity:
    engine_capacity_choices = [('engine_capacity_less_than', 'Equal or less than:'),
                               ('engine_capacity_more_than', 'Equal or more than:'),
                               ('engine_capacity_equal', 'Exact:')]
    engine_capacity_less_more = forms.ChoiceField(widget=forms.RadioSelect, choices=engine_capacity_choices, required=False)
    engine_capacity = forms.FloatField(required=False)

    # Engine power:
    engine_power_choices = [('engine_power_less_than', 'Equal or less than:'),
                            ('engine_power_more_than', 'Equal or more than:'),
                            ('engine_power_equal', 'Exact:')]
    engine_power_less_more = forms.ChoiceField(widget=forms.RadioSelect, choices=engine_power_choices, required=False)
    engine_power = forms.IntegerField(required=False)

    def clean(self):
        mileage_less_more = self.cleaned_data.get('mileage_less_more')

        if mileage_less_more:
            self.fields_below_required(['mileage'])

        production_year_less_more = self.cleaned_data.get('production_year_less_more')

        if production_year_less_more:
            self.fields_below_required(['production_year'])

        price_less_more_choices = self.cleaned_data.get('price_less_more_choices')

        if price_less_more_choices:
            self.fields_below_required(['price'])
            self.fields_below_required(['price_currency'])

        engine_capacity_less_more = self.cleaned_data.get('engine_capacity_less_more')

        if engine_capacity_less_more:
            self.fields_below_required(['engine_capacity'])

        engine_power_less_more = self.cleaned_data.get('engine_power_less_more')

        if engine_power_less_more:
            self.fields_below_required(['engine_power'])

        return self.cleaned_data

    def fields_below_required(self, fields):
        """Used for conditionally marking fields as required."""
        for field in fields:
            if not self.cleaned_data.get(field, ''):
                msg = forms.ValidationError("If you selected option above then this field is required now:")
                self.add_error(field, msg)
