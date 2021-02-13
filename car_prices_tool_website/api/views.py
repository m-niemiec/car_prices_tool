from datetime import date
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .serializers import CarSerializer
from car_prices_tool.models import UserPremiumRank, UserSearchQuery, Car
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.authtoken.models import Token


@csrf_exempt
def sign_up_user(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(username=data['username'], password=data['password'])
            user.save()

            context = {
                'message': 'Thank you for registering!'
            }

            return JsonResponse(context, status=201)
        except IntegrityError:
            context = {
                'error': 'This username is already taken. Please choose another one.'
            }

            return JsonResponse(context, status=400)


@csrf_exempt
def get_token(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is None:
            context = {
                'error': 'Wrong password or user.'
            }

            return JsonResponse(context)
        else:
            try:
                user_rank = UserPremiumRank.objects.filter(user=user).values('rank').get()
            except UserPremiumRank.DoesNotExist:
                user_rank = {}

            if user_rank.get('rank') == 'APIPRO':
                try:
                    token = Token.objects.get(user=user)
                except Token.DoesNotExist:
                    token = Token.objects.create(user=user)

                context = {
                    'token': str(token)
                }

                return JsonResponse(context, status=200)
            else:
                context = {
                    'error': 'You need rank API Pro to get your own API Key / Token!'
                }

                raise ValidationError(detail=context)


class CarsResults(generics.ListAPIView):
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        try:
            user_rank = UserPremiumRank.objects.filter(user=user).values('rank').get()
        except UserPremiumRank.DoesNotExist:
            user_rank = {}

        today = date.today()
        last_user_searches = UserSearchQuery.objects.filter(user=user, date__year=today.year,
                                                            date__month=today.month, date__day=today.day).count()

        filters = {}

        if user_rank.get('rank') == 'APIPRO':
            if last_user_searches < 500:
                new_search = UserSearchQuery(user=user, search_parameters=filters)
                new_search.save()

                return Car.objects.filter(**filters)[:30]
            else:
                context = {
                    'error': 'No searches left for today!'
                }

                raise ValidationError(detail=context)
        else:
            context = {
                'error': 'Sorry, it looks like you do not have API Pro account.'
            }

            raise ValidationError(detail=context)


class CarCreate(generics.ListCreateAPIView):
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return Car.objects.order_by('-date_scraped')[:10]

    def perform_create(self, serializer):
        serializer.save()


class CarRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return Car.objects
