from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
# from Propiedades.form import LoginForm
from Propiedades.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
# from django.contrib.auth import authenticate, logout, login as auth_login
# from django.contrib import messages
# Create your views here.

def index(request):
    template_name = "index.html"
    return render(request, template_name, {})

def list_property(request):
    #si es false el super admin no podra entrar
    data = {}

    data["request"] = request
    a = request
    print(a)
    object_list = Property.objects.all().order_by('-id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)
    template_name = 'list_property.html'
    return render(request, template_name, data)

# def login(request):
#     template_name = 'login.html'
#     data = {}
#
#     username = password = ''
#
#     if request.POST:
#         username = request.POST.get('user')
#         password = request.POST.get('password')
#         print('-------------------------------------')
#         print(username)
#         print(password)
#         print('-------------------------------------')
#         user = authenticate(
#             username=username,
#             password=password
#         )
#         print('-------------------------------------')
#         print(user)
#         print('-------------------------------------')
#         if user is not None:
#             if user.is_active:
#                 auth_login(request, user)
#                 return render(request, 'list_property.html')
#             else:
#                 print("usuario o contraseña no validos")
#                 messages.warning(
#                     request,
#                     'Usuario o contraseña incorrectos!'
#                 )
#         else:
#             print("Usuario incorrecto")
#             messages.error(
#                 request,
#                 'Usuario o contraseña incorrectos!'
#             )
#     return render(request, template_name, data)
#
#
# def auth_logout(request):
#     logout(request)
#     return render(request, template_name, {})