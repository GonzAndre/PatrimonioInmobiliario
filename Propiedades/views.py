from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from Propiedades.models import *
from Propiedades.forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
# Create your views here.

def index(request):
    template_name = "index.html"

    return render(request, template_name, {})

def list_acquisition(request):
    data = {}
    data["request"] = request

    object_list = Acquisition.objects.all().order_by('-id')
    print (object_list)

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

def view_acquisition(request, cli_id):
    data = {}
    data['request'] = request
    template_name = 'detail_acquisition.html'
    data ['acquisition'] = Acquisition.objects.get(pk=cli_id)
    return render(request, template_name, data)

def list_rent(request):
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
    template_name = 'list_rent.html'
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
            return redirect('list_acquisitions')
    else:
        form = AcquisitionForm()

    template_name = 'add_acquisition.html'
    return render(request, template_name, {'form':form})

def Add_rent(request):
    data={}
    data["request"] = request
    if request.method == "POST":
        data['form'] = RentForm(request.POST,request.FILES)

        if data['form'].is_valid():
            sav = data['form'].save()
            return redirect('list_rent')
    else:
        form = RentForm()

    template_name = 'add_rent.html'
    return render(request, template_name, {'form':form})

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