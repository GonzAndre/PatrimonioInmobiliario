from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from propiedades2.models import Acquisition, Document, Rent, Location, Post
from propiedades2.forms import DocumentForm, LocationForm, AcquisitionForm, ArquitectureForm, \
    InternalForm, NotaryForm, SII_recordForm, RentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


# Create your views here.

def index(request):
    return render(request, 'index.html', {'cosa': 'pat'})


@login_required(login_url='login')
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


# agregar todas las weas vacias

@login_required(login_url='login')
def view_acquisition(request, cli_id):
    data = {}
    template_name = 'detail_acquisition.html'
    data['acquisition'] = Acquisition.objects.get(pk=cli_id)
    return render(request, template_name, data)


@login_required(login_url='login')
def view_rent(request, rent_id):
    data = {}
    template_name = 'detail_rent.html'
    data['rent'] = Rent.objects.get(pk=rent_id)
    return render(request, template_name, data)


@login_required(login_url='login')
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


@login_required(login_url='login')
def Add_acquisition(request):
    data = {}
    if request.method == "POST":
        # ArquitectureForm,InternalForm,NotaryForm,SII_recordForm
        data['formAcquisition'] = AcquisitionForm(request.POST, request.FILES)
        data['formLocation'] = LocationForm(request.POST, request.FILES)
        # Arquitecture
        data['formArquitecture'] = ArquitectureForm(request.POST, request.FILES)
        data['formEx'] = DocumentForm(request.POST, request.FILES)
        data['formCip'] = DocumentForm(request.POST, request.FILES)
        data['formCn'] = DocumentForm(request.POST, request.FILES)
        data['formBlue'] = DocumentForm(request.POST, request.FILES)
        data['formBuildP'] = DocumentForm(request.POST, request.FILES)
        data['formMR'] = DocumentForm(request.POST, request.FILES)
        # Internal
        data['formInternal'] = InternalForm(request.POST, request.FILES)
        data['formTypeC'] = DocumentForm(request.POST, request.FILES)
        data['formOther'] = DocumentForm(request.POST, request.FILES)
        # Notary
        data['formNotary'] = NotaryForm(request.POST, request.FILES)
        data['formWR'] = DocumentForm(request.POST, request.FILES)
        data['formDC'] = DocumentForm(request.POST, request.FILES)
        data['formPH'] = DocumentForm(request.POST, request.FILES)
        data['formEs'] = DocumentForm(request.POST, request.FILES)
        # Sii
        data['formSII'] = SII_recordForm(request.POST, request.FILES)
        data['formAc'] = DocumentForm(request.POST, request.FILES)
        data['formDB'] = DocumentForm(request.POST, request.FILES)

        print('request: ',request.POST)

        if request.POST['Tipo'] == "Propiedad":
            if data['formAcquisition'].is_valid():
                data['formAcquisition'] = data['formAcquisition'].save(commit=False)
                if data['formLocation'].is_valid():
                    data['formLocation'] = data['formLocation'].save()
                    aux = Location.objects.get(pk=data['formLocation'].pk)
                    data['formAcquisition'].location = aux
                    data['formAcquisition'].save()
                    return JsonResponse({'id': data['formAcquisition'].pk})

        elif request.POST['Tipo'] == "arquitecture":
            print('Funciona antes de validar')
            if data['formArquitecture'].is_valid():
                arquitectureForm = data['formArquitecture'].save(commit=False)
                print(request.POST['docEx'])
                if data['formEx'].is_valid():
                    print("formulario ex valido")
                    Ex = data['formEx']
                    Ex.type = 'EM'
                    arquitectureForm.expropriation_mun = Ex.save()
                    if data['formCip'].is_valid():
                        cip = data['formCip']
                        cip.type = 'CP'
                        arquitectureForm.cip = cip.save()
                        if data['formCn'].is_valid():
                            Cn = data['formCn']
                            Cn.type = 'Nc'
                            arquitectureForm.certified_number = Cn.save()
                            if data['formBlue'].is_valid():
                                Blue = data['formBlue']
                                Blue.type = 'PL'
                                arquitectureForm.blueprints = Blue.save()
                                if data['formBuildP'].is_valid():
                                    Build = data['formBuildP']
                                    Build.type = 'PE'
                                    arquitectureForm.building_permit = Build.save()
                                    if data['formMR'].is_valid():
                                        print("Ultimo valido")
                                        MR = data['formMR']
                                        MR.type = 'RM'
                                        arquitectureForm.municipal_reception = MR.save()
                                        arquitectureForm.save()
                                        return JsonResponse({})

        elif request.POST['Tipo'] == 'Internal':
            if data['formInternal'].is_valid():
                data['formInternal'] = data['formInternal'].save(commit=False)
                if data['formTypeC'].is_valid():
                    data['formTypeC'].type = 'TC'
                    data['formInternal'].contract_type = data['formTypeC'].save()
                    if data['formOther'].is_valid():
                        data['formOther'].type = 'OT'
                        data['formInternal'].others = data['formOther'].save()
                        data['formInternal'].save()
                        # guardar en acquisition el intenal
                        return JsonResponse({})

        elif request.POST['Tipo'] == 'Notary':
            if data['formNotary'].is_valid():
                data['formNotary'] = data['formNotary'].save(commit=False)
                if data['formWR'].is_valid():
                    data['formWR'].type = 'ES'
                    data['formNotary'].writing = data['formWR'].save()
                    if data['formDC'].is_valid():
                        data['formDC'].type = 'CD'
                        data['formNotary'].domain_certificate = data['formDC'].save()
                        if data['formPH'].is_valid():
                            data['formPH'].type = 'PR'
                            data['formNotary'].prohibitions = data['formPH'].save()
                            if data['formEs'].is_valid():
                                data['formEs'].type = 'SE'
                                data['formNotary'].expropriation_serviu = data['formEs'].save()
                                data['formNotary'].save()
                                return JsonResponse({})

        elif request.POST['Tipo'] == 'SII':
            if data['formSII'].is_valid():
                data['formSII'] = data['formSII'].save(commit=False)
                if data['formAc'].is_valid():
                    data['formAc'].type = 'CA'
                    data['formSII'].appraisal_certificate = data['formAc'].save()
                    if data['formDB'].is_valid():
                        data['formDB'].type = 'CD'
                        data['formSII'].debt_certificate = data['formDB'].save()
                        data['formSII'].save()
                        return JsonResponse({})

    else:
        data = {
            'formLocation': LocationForm, 'formAcquisition': AcquisitionForm, 'formArquitecture': ArquitectureForm,
            'formEx': DocumentForm, 'formCip': DocumentForm, 'formCn': DocumentForm,
            'formBlue': DocumentForm,
            'formBuildP': DocumentForm, 'formMR': DocumentForm, 'formInternal': InternalForm,
            'formTypeC': DocumentForm,
            'formOther': DocumentForm, 'formNotary': NotaryForm, 'formWR': DocumentForm,
            'formDC': DocumentForm,
            'formPH': DocumentForm, 'formEs': DocumentForm, 'formSII': SII_recordForm,
            'formAc': DocumentForm, 'formDB': DocumentForm,
        }

    return render(request, 'add_acquisition.html', data)


@login_required(login_url='login')
def Add_rent(request):
    data = {}
    if request.method == "POST":
        data['formLocation'] = LocationForm(request.POST)
        data['formRent'] = RentForm(request.POST, request.FILES)
        data['formDocument'] = DocumentForm(request.POST, request.FILES)

        if data['formRent'].is_valid():
            rent = data['formRent'].save(commit=False)
            if data['formLocation'].is_valid():
                location = data['formLocation'].save()
                rent.location = location
                if data['formDocument'].is_valid():
                    document = data['formDocument'].save()
                    rent.contract_type = document
                    rent.save()
            return redirect('list_rent')
    else:
        formDocument = DocumentForm()
        formLocation = LocationForm()
        formRent = RentForm()

    return render(request, 'add_rent.html',
                  {'formDocument': formDocument, 'formLocation': formLocation, 'formRent': formRent})


@login_required(login_url='login')
def Edit_acquisition(request, acq_id):
    data = {}
    if request.POST:
        AcquisitionForm = EditAcquisition(request.POST, request.FILES, instance=Acquisition.objects.get(pk=acq_id))
        if AcquisitionForm.is_valid():
            AcquisitionForm.save()
            return redirect('list_acquisitions')
    template_name = 'edit.html'
    data['data'] = EditAcquisition(instance=Acquisition.objects.get(pk=acq_id))

    return render(request, template_name, data)


@login_required(login_url='login')
def Edit_rent(request, rent_id):
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


@login_required(login_url='login')
def Delete_acquisition(request, id):
    data = {}
    template_name = ''
    data['acquisition'] = Acquisition.objects.all()
    Acquisition.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse('list_acquisition'))


@login_required(login_url='login')
def Delete_rent(request):
    data = {}
    template_name = ''
    data['rent'] = Rent.objects.all()
    Rent.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse('list_rent'))


@login_required(login_url='login')
def view_archive(request, document_id):
    data = {}
    data['request'] = request
    template_name = 'view_archive.html'
    if document_id != None:
        data['archive'] = Document.objects.get(pk=document_id)
        return render(request, template_name, data)

    else:
        return render(request, template_name)


@login_required(login_url='login')
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
