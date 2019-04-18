from django.shortcuts import render
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login(request):
    template_name = 'login.html'
    data = {}
    auth_logout(request)
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
                return HttpResponseRedirect(reverse('list_property'))
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

@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('login'))