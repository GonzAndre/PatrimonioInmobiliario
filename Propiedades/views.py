from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
# from Propiedades.form import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from Propiedades.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
import re
from django.contrib import messages
# Create your views here.

def index(request):
    template_name = "base.html"

    return render(request, template_name, {})

@login_required(login_url='login')
def list_acquisition(request):
    #si es false el super admin no podra entrar
    data = {}

    data["request"] = request
    object_list = Acquisition.objects.all().order_by('id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)
    template_name = 'list_acquisition.html'
    return render(request, template_name, data)

def list_rent(request):
    #si es false el super admin no podra entrar
    data = {}
    data["request"] = request

    object_list = Rent.objects.all().order_by('id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)
    template_name = 'list_rent.html'
    return render(request, template_name, data)

def list_total(request):
    data = {}
    object_list_acquisition = Acquisition.objects.all().order_by('id')
    object_list_rent = Rent.objects.all().order_by('id')
    paginator_acq = Paginator(object_list_acquisition, 5)
    paginator_rent = Paginator(object_list_rent, 5)
    page = request.GET.get('page')

    try:
        data['object_list_acquisition'] = paginator_acq.page(page)
        data['object_list_rent'] = paginator_rent.page(page)
    except PageNotAnInteger:
        data['object_list_acquisition'] = paginator_acq.page(1)
        data['object_list_rent'] = paginator_rent.page(1)
    except EmptyPage:
        data['object_list_acquisition'] = paginator_acq.page(paginator_acq.num_pages)
        data['object_list_rent'] = paginator_rent.page(paginator_rent.num_pages)
    template_name = 'list_total.html'
    return render(request, template_name, data)


def Add_acquisition(request):

    data = {}
    data["request"] = request
    if request.method == "POST":
        data['form'] = AcquisitionForm(request.POST,request.FILES)

        if data['form'].is_valid():
            sav = data['form'].save()
            return redirect('list_acquisition')
        else:
            data['form'] = AcquisitionForm()

    template_name = 'add_acquisition.html'
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

@login_required(login_url='login')
def view_acquisition(request, cli_id):
    data = {}
    data['request'] = request
    template_name = 'detail_acquisition.html'
    data ['acquisition'] = Acquisition.objects.get(pk=cli_id)
    print('------------------------')
    print(data)
    print('------------------------')
    return render(request, template_name, data)

@login_required(login_url='login')
def view_rent(request, rent_id):
    data = {}
    data['request'] = request
    template_name = 'detail_rent1.html'
    data ['rent'] = Rent.objects.get(pk=rent_id)
    return render(request, template_name, data)

def view_archive(request, document_id):
    data = {}
    data['request'] = request
    template_name = 'view_archive.html'
    if document_id != None:
        data['archive'] = Document.objects.get(pk=document_id)
        print('-------------------------------')
        print(data)
        print('-------------------------------')
        return render(request, template_name, data)

    else:
        return render(request, template_name)


def search(request):
    template = 'search.html'

    data = {}
    data[request] = request
    query = request.GET.get('q')
    # objects_list = list(Acquisition.objects.all())
    object_list_acquisition = Acquisition.objects.filter(Q(property_use=query) | Q(name__contains=query)).order_by('id')
    object_list_rent = Rent.objects.filter(Q(property_use=query) | Q(name__contains=query)).order_by('id')
    paginator_acq = Paginator(object_list_acquisition, 5)
    paginator_rent = Paginator(object_list_rent, 5)
    page = request.GET.get('page')
    try:
        data['object_list_acquisition'] = paginator_acq.page(page)
        data['object_list_rent'] = paginator_rent.page(page)
    except PageNotAnInteger:
        data['object_list_acquisition'] = paginator_acq.page(1)
        data['object_list_rent'] = paginator_rent.page(1)
    except EmptyPage:
        data['object_list_acquisition'] = paginator_acq.page(paginator_acq.num_pages)
        data['object_list_rent'] = paginator_rent.page(paginator_rent.num_pages)
    return render(request, template, data)


