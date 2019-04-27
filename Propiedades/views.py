from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from Propiedades.models import Acquisition,Document,Rent,Location,Post
from Propiedades.forms import DocumentForm,LocationForm,AcquisitionForm,RentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'index.html', {'cosa': 'pat'})


def list_acquisition(request):
    data = {}
    object_list = Acquisition.objects.all().order_by('-id')
    print(object_list)

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
    template_name = 'detail_acquisition.html'
    data['acquisition'] = Acquisition.objects.get(pk=cli_id)
    return render(request, template_name, data)


def view_rent(request, rent_id):
    data = {}
    data_documents = {}
    template_name = 'detail_rent.html'
    data['rent'] = Rent.objects.get(pk=rent_id)
    data_documents['document'] = Document.objects.get(pk=rent_id)
    return render(request, template_name, data, data_documents)


def list_rent(request):
    data = {}

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
    if (Leadership):
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
    if request.method == "POST":
        data['form'] = AcquisitionForm(request.POST, request.FILES)
        data['form2'] = LocationForm(request.POST, request.FILES)

        if data['form'].is_valid() and data['form2'].is_valid():
            print('Hola 1')
            sav = data['form'].save(commit=False)
            print('Hola 2')
            sav.location = data['form2'].save()
            print('Hola 3')
            sav.save()
            print('Hola 4')
        return redirect('list_acquisitions')
    else:
        form2 = LocationForm()
        form = AcquisitionForm()

    return render(request, 'add_acquisition.html', {'form': form,'form2': form2})


def Add_rent(request):
    data = {}
    if request.method == "POST":
        data['form'] = RentForm(request.POST, request.FILES)
        data['form2'] = LocationForm(request.POST)

        if data['form'].is_valid() and data['form2'].is_valid():
            sav = data['form'].save(commit=False)
            sav.Location = data[form2].save()
            return redirect('list_rent')
    else:
        form2 = LocationForm()
        form = RentForm()

    return render(request, 'add_rent.html', {'form': form,'form2': form2})


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
