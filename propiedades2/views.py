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


        if data['formAcquisition'].is_valid():
            sav = data['formAcquisition'].save(commit=False)
            if data['formLocation'].is_valid():
                locationForm = data['formLocation'].save()
                sav.location = locationForm
                if data['formArquitecture'].is_valid():
                    arquitectureForm = data['formArquitecture'].save(commit=False)
                    if data['formEx'].is_valid():
                        Ex = data['formEx']
                        Ex.type = 'EM'
                        arquitectureForm.expropriation_mun = Ex.save()
                    elif data['formCip'].is_valid():
                        cip = data['formCip']
                        cip.type = 'CP'
                        arquitectureForm.cip = cip.save()
                    elif data['formCn'].is_valid():
                        Cn = data['formCn']
                        Cn.type = 'Nc'
                        arquitectureForm.certified_number =Cn.save()
                    elif data['formBlue'].is_valid():
                        Blue = data['formBlue']
                        Blue.type = 'PL'
                        arquitectureForm.blueprints = Blue.save()
                    elif data['formBuildP'].is_valid():
                        Build = data['formBuildP']
                        Build.type = 'PE'
                        arquitectureForm.building_permit = Build.save()
                    elif data['formMR'].is_valid():
                        MR = data['formMR']
                        MR.type = 'RM'
                        arquitectureForm.municipal_reception = MR.save()

                    arquitectureForm.save()
                    sav.arquitecture = arquitectureForm

                if data['formInternal'].is_valid():
                    internalForm = data['formInternal'].save(commit=False)
                    if data['formTypeC'].is_valid():
                        TC = data['formTypeC']
                        TC.type = 'TC'
                        internalForm.contract_type = TC.save()
                    elif data['formOther'].is_valid():
                        OT = data['formOther']
                        OT.type = 'OT'
                        internalForm.others = OT.save()

                    internalForm.save()
                    sav.internal = internalForm

                if data['formNotary'].is_valid():
                    notaryForm = data['formNotary'].save(commit=False)
                    if data['formWR'].is_valid():
                        WR = data['formWR']
                        WR.type = 'ES'
                        notaryForm.writing = WR.save()
                    elif data['formDC'].is_valid():
                        DC = data['formDC']
                        DC.type = 'CD'
                        notaryForm.domain_certificate = DC.save()
                    elif data['formPH'].is_valid():
                        PH = data['formPH']
                        PH.type = 'PR'
                        notaryForm.prohibitions = PH.save()
                    elif data['formEs'].is_valid():
                        Es = data['formEs']
                        Es.type = 'SE'
                        notaryForm.expropriation_serviu = Es.save()

                    notaryForm.save()
                    sav.notary = notaryForm

                if data['formSII'].is_valid():
                    siiForm = data['formSII'].save(commit=False)
                    if data['formAc'].is_valid():
                        Ac = data['formAc']
                        Ac.type = 'CA'
                        siiForm.appraisal_certificate = Ac.save()
                    elif data['formDB'].is_valid():
                        DB = data['formDB']
                        DB.type = 'CD'
                        siiForm.debt_certificate = data['formDB'].save()

                    siiForm.save()
                    sav.SII = siiForm

            sav.save()
        return redirect('list_acquisitions')
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
        data['formDocument'] = DocumentForm(request.POST,request.FILES)

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

    return render(request, 'add_rent.html', {'formDocument': formDocument, 'formLocation': formLocation,'formRent':formRent})

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def Delete_acquisition(request):
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