from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from propiedades2.models import Acquisition,Document,Rent,Location,Post
from propiedades2.forms import DocumentForm,LocationForm,AcquisitionForm,ArquitectureForm,InternalForm,NotaryForm,SII_recordForm,RentForm
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
        data['formNotary'] = NotaryForm(request.POST,request.FILES)
        data['formWR'] = DocumentForm(request.POST,request.FILES)
        data['formDC'] = DocumentForm(request.POST,request.FILES)
        data['formPH'] = DocumentForm(request.POST,request.FILES)
        data['formEs'] = DocumentForm(request.POST,request.FILES)
        # Sii
        data['formSII'] = SII_recordForm(request.POST,request.FILES)
        data['formAc'] = DocumentForm(request.POST,request.FILES)
        data['formDB'] = DocumentForm(request.POST,request.FILES)

        if data['formAcquisition'].is_valid():
            sav = data['formAcquisition'].save(commit=False)
            if data['formLocation'].is_valid():
                locationForm = data['formLocation'].save()
                sav.location = locationForm
                print('hola arquitecture')
                if data['formArquitecture'].is_valid():
                    arquitectureForm = data['formArquitecture'].save(commit=False)
                    if data['formEx'].is_valid():
                        arquitectureForm.expropriation_mun = data['formEx']
                    elif data['formCip'].is_valid():
                        arquitectureForm.cip = data['formCip']
                    elif data['formCn'].is_valid():
                        arquitectureForm.certified_number = data['formCn']
                    elif data['formBlue'].is_valid():
                        arquitectureForm.blueprints = data['formBlue']
                    elif data['formBuildP'].is_valid():
                        arquitectureForm.building_permit = data['formBuildP']
                    elif data['formMR'].is_valid():
                        arquitectureForm.municipal_reception = data['formMR']

                    arquitectureForm.save()
                    sav.arquitecture = arquitectureForm

                    if data['formInternal'].is_valid():
                        internalForm = data['formInternal'].save(commit=False)
                        if data['formTypeC'].is_valid():
                            internalForm.contract_type = data['formTypeC']
                        elif data['formOther'].is_valid():
                            internalForm.others = data['formOther']

                        internalForm.save()
                        sav.internal = internalForm

                        if data['formNotary'].is_valid():
                            notaryForm = data['formNotary'].save(commit=False)
                            if data['formWR'].is_valid():
                                notaryForm.writing = data['formWR']
                            elif data['formDC'].is_valid():
                                notaryForm.domain_certificate = data['formDC']
                            elif data['formPH'].is_valid():
                                notaryForm.prohibitions = data['formPH']
                            elif data['formEs'].is_valid():
                                notaryForm.expropriation_serviu = data['formEs']

                            notaryForm.save()
                            sav.notary = notaryForm

                            if data['formSII'].is_valid():
                                siiForm = data['formSII'].save(commit=False)
                                if data['formAc'].is_valid():
                                    siiForm.appraisal_certificate = data['formAc']
                                elif data['formDB'].is_valid():
                                    siiForm.debt_certificate = data['formDB']

                                siiForm.save()
                                sav.SII = siiForm

            sav.save()
        return redirect('list_acquisitions')
    else:
        data = {
            'formLocation': LocationForm, 'formAcquisition': AcquisitionForm, 'formArquitecture': ArquitectureForm,
            'formEx' : DocumentForm, 'formCip': DocumentForm, 'formCn': DocumentForm, 'formBlue': DocumentForm,
            'formBuildP': DocumentForm, 'formMR': DocumentForm, 'formInternal': InternalForm, 'formTypeC': DocumentForm,
            'formOther': DocumentForm, 'formNotary': NotaryForm, 'formWR': DocumentForm, 'formDC': DocumentForm,
            'formPH': DocumentForm, 'formEs': DocumentForm, 'formSII': SII_recordForm, 'formAc': DocumentForm, 'formDB': DocumentForm,
        }

    return render(request, 'add_acquisition.html', data)


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
