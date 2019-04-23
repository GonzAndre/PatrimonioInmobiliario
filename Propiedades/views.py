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
    template_name = "base.html"

    return render(request, template_name, {})

def list_acquisition(request):
    #si es false el super admin no podra entrar
    data = {}
    data["request"] = request

    object_list = Acquisition.objects.all().order_by('-id')

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

def list_rent(request):
    #si es false el super admin no podra entrar
    data = {}
    data["request"] = request

    object_list = Rent.objects.all().order_by('-id')

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

def Add_acquisition(request):

    data = {}
    data["request"] = request
    if request.method == "POST":
        data['form'] = AcquisitionForm(request.POST,request.FILES)

        if data['form'].is_valid():
            sav = data['form'].save()
            return redirect('list_property')
        else:
            data['form'] = AcquisitionForm()

    template_name = 'add_property.html'
    return render(request, template_name, data)

def Add_rent(request):
    data={}
    data["request"] = request
    if request.method == "POST":
        data['form'] = RentForm(request.POST,request.FILES)

        if data['form'].is_valid():
            sav = data['form'].save()
            return redirect('list_rent')
        else:
            data['form'] = RentForm()

    template_name = 'add_property.html'
    return render(request, template_name, data)

def Edit_acquisition(request):
    data = {}
    data["request"] = request
    if request.POST:
        AcquisitionForm = EditAcquisition(request.POST, request.FILES, instance=Acquisition.objects.get(pk=acq_id))
        if AcquisitionForm.is_valid():
            AcquisitionForm.save()
            return redirect('list_acquisitions')
    template_name = 'edit.html'
    data['data'] = EditAcquisition(instance=Acquisition.objects.get(pk=acq_id))

    return render(request, template_name, data)

def Edit_rent(request):
    data = {}
    data["request"] = request
    if request.POST:
        RentForm = EditRent(request.POST, request.FILES, instance=Rent.objects.get(pk=rent_id))
        if RentForm.is_valid():
            RentForm.save()
            return redirect('list_rent')
    template_name = 'edit.html'
    data['data'] = EditRent(instance=Rent.objects.get(pk=rent_id))

    return render(request, template_name, data)

def Delete_acquisition(request):
    data = {}
    template_name = ''
    data['acquisition'] = Acquisition.objects.all()
    Acquisition.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse('list_acquisition'))

def Delete_rent(request):
    data = {}
    template_name = ''
    data['rent'] = Rent.objects.all()
    Rent.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse('list_rent'))