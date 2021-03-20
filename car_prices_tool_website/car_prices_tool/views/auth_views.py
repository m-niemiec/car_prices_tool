from django import template
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect

register = template.Library()


def sign_up_user(request):
    if request.method == 'GET':
        context = {
            'form': UserCreationForm()
        }

        return render(request, 'car_prices_tool/signup.html', context)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)

                return redirect('search')
            except IntegrityError:
                context = {
                    'form': UserCreationForm(),
                    'error': 'This username is already taken. Please choose another one.'
                }

                return render(request, 'car_prices_tool/signup.html', context)
        else:
            context = {
                'form': UserCreationForm(),
                'error': 'Password did not match!'
            }

            return render(request, 'car_prices_tool/signup.html', context)


def log_in_user(request):
    if request.method == 'GET':
        context = {
            'form': AuthenticationForm()
        }

        return render(request, 'car_prices_tool/login.html', context)
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)

            return redirect('search')
        else:
            context = {
                'form': AuthenticationForm(),
                'error': 'Wrong password or username.'
            }

            return render(request, 'car_prices_tool/login.html', context)


def log_out_user(request):
    if request.method == 'POST':
        logout(request)

        return render(request, 'car_prices_tool/home.html')