from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login as auth_login
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages


def login(request):
    template_name = 'login.html'
    data = {}

    username = password = ''

    if request.POST:
        username = request.POST.get('user')
        password = request.POST.get('password')
        print('-------------------------------------')
        print(username)
        print(password)
        print('-------------------------------------')
        user = authenticate(
            username=username,
            password=password
        )
        print('-------------------------------------')
        print(user)
        print('-------------------------------------')
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return render(request, 'list_property.html')
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


def auth_logout(request):
    logout(request)
    return render(request, template_name, {})