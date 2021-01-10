from django.db import models
from django.contrib.auth.models import User
from django.db.models import JSONField


class CarMake(models.Model):
    car_make = models.CharField(max_length=50)

    def __str__(self):
        return self.car_make


class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    model_variant = models.CharField(max_length=50)
    production_year = models.IntegerField()
    engine_power = models.IntegerField()
    mileage = models.IntegerField()
    engine_capacity = models.FloatField()
    offer_type = models.CharField(max_length=10)
    price = models.IntegerField()
    price_currency = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    price_dollars = models.IntegerField()

    def __str__(self):
        return self.make


class UserSearchQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    search_parameters = JSONField()


class UserPremiumRank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rank = models.CharField(max_length=50)
