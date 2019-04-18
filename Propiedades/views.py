from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
# from Propiedades.form import LoginForm
from Propiedades.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, logout, login as auth_login
# from django.contrib import messages
# Create your views here.

def index(request):
    template_name = "index.html"
    return render(request, template_name, {})

@login_required(login_url='login')
def list_property(request):
    #si es false el super admin no podra entrar
    data = {}

    data["request"] = request
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

@login_required(login_url='login')
def view_acquisition(request, cli_id):
    data = {}
    data['request'] = request
    template_name = 'detail_acquisition.html'
    data ['acquisition'] = Acquisition.objects.get(pk=cli_id)
    print(data)
    return render(request, template_name, data)
