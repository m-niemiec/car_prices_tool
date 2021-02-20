import pytest
from django.urls import reverse
# from django.contrib.auth.models import User
# from django.test import RequestFactory
# from mixer.backend.django import mixer
# from car_prices_tool.views import results


@pytest.mark.django_db
class TestViews:
    def test_home_view(self, client):
        url = reverse('home')
        response = client.get(url)
        assert response.status_code == 200

    def test_about_view(self, client):
        url = reverse('about')
        response = client.get(url)
        assert response.status_code == 200

    def test_features_view(self, client):
        url = reverse('features')
        response = client.get(url)
        assert response.status_code == 200

    def test_pricing_view(self, client):
        url = reverse('pricing')
        response = client.get(url)
        assert response.status_code == 200

    def test_sign_up_user_view(self, client):
        url = reverse('signup')
        response = client.get(url)
        assert response.status_code == 200

    def test_log_in_user_view(self, client):
        url = reverse('login')
        response = client.get(url)
        assert response.status_code == 200

    def test_load_models_view(self, client):
        url = reverse('ajax_load_models')
        response = client.get(url)
        assert response.status_code == 200

    # def test_results(self):
    #     path = reverse('results')
    #     request = RequestFactory().get(path)
    #     request.user = mixer.blend(User)
    #
    #     response = results(request)
    #     assert response.status_code == 200
