import pendulum
from datetime import date
from rest_framework import generics, permissions
from .serializers import CarSerializer
from car_prices_tool.models import UserPremiumRank, UserSearchQuery, Car


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

        if user_rank.get('rank') == 'Premium':
            if last_user_searches < 100:
                # new_search = UserSearchQuery(user=user, search_parameters=filters)
                # new_search.save()

                return Car.objects.filter(**filters)[:30]
            else:
                context = {
                    'quota_error': 'No searches left for today!'
                }

                return context
        else:
            context = {
                'authorization_error': 'Sorry, it looks like you cannot access this resources.'
            }

            return context


class CarCreate(generics.ListCreateAPIView):
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return Car.objects.order_by('-date_scraped')[:10]

    def perform_create(self, serializer):
        serializer.save()
