from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
# from Propiedades.form import LoginForm
from django.contrib.auth import authenticate, login, logout
from Propiedades.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
# Create your views here.

def index(request):
    template_name = "index.html"
    return render(request, template_name, {})

# def login1(request):
#     template_name = 'login.html'
#     data = {}
#
#     logout(request)
#     username = password = ''
#
#     if request.POST:
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = authenticate(
#             username=username,
#             password=password
#         )
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return render(request, 'index.html', data)
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
# def auth_logout(request):
#     logout(request)
#     return render(request, 'admin.html', data)


def list_property(request):
    #si es false el super admin no podra entrar
    data = {}

    data["request"] = request
    a = request
    print('-------------')
    print(a)
    print('-------------')
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