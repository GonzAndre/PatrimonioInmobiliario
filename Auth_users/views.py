from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from Propiedades.models import *

def login(request):
    template_name = 'login.html'
    data = {}

    logout(request)
    username = password = ''

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        print(username)
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        print(password)
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

        username = authenticate(
            username=username,
            password=password
        )
        if username is not None:
            if username.is_active:
                login(request, username)
                return render(request, template_name, data)
            else:
                print("usuario o contraseña no validos")
                messages.warning(
                    request,
                    'Usuario o contraseña incorrectos!'
                )
        else:
            print("Usuario incorrecto")
            messages.error(
                request,
                'Usuario o contraseña incorrectos!'
            )
    return render(request, template_name, data)


def logout(request):
    logout(request)
    return render(request, 'login.html', data)

def user_leaderships(UserProfile, Leadership):
    if(Leadership):
        try:
            Leadership.objects.get(UserProfile=UserProfile)
            return False
        except Exception as e:
            return True
    else:
        try:
            Leadership.objects.get(UserProfile=UserProfile)
            return True
        except Exception as e:
            return False