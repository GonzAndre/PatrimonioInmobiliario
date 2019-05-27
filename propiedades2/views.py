from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from propiedades2.models import Acquisition, DocumentEx, DocumentCip, DocumentCn, DocumentBlue, DocumentBuildP, \
    DocumentMR, DocumentTypeC, DocumentOther, DocumentWR, DocumentDC, DocumentPH, DocumentDB, DocumentAc, DocumentEs, \
    Rent, Location, Post
from propiedades2.forms import DocExForm, DocCipForm, DocCnForm, DocBlueForm, DocBuildPForm, DocMRForm, DocTypeCForm, \
    DocOtherForm, DocWRForm, DocDCForm, DocPHForm, DocDBForm, DocAcForm, DocEsForm, LocationForm, AcquisitionForm, \
    ArquitectureForm, InternalForm, NotaryForm, SII_recordForm, RentForm, DocExForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q


# Create your views here.

def index(request):
    return render(request, 'index.html', {'cosa': 'pat'})


@login_required(login_url='login')
def list_acquisition(request):
    data = {}
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
    id_propiedad = 0
    if request.method == "POST":
        # ArquitectureForm,InternalForm,NotaryForm,SII_recordForm
        data['formAcquisition'] = AcquisitionForm(request.POST, request.FILES)
        data['formLocation'] = LocationForm(request.POST, request.FILES)
        # Arquitecture
        data['formArquitecture'] = ArquitectureForm(request.POST, request.FILES)
        data['formEx'] = DocExForm(request.POST, request.FILES)
        data['formCip'] = DocCipForm(request.POST, request.FILES)
        data['formCn'] = DocCnForm(request.POST, request.FILES)
        data['formBlue'] = DocBlueForm(request.POST, request.FILES)
        data['formBuildP'] = DocBuildPForm(request.POST, request.FILES)
        data['formMR'] = DocMRForm(request.POST, request.FILES)
        # Internal
        data['formInternal'] = InternalForm(request.POST, request.FILES)
        data['formTypeC'] = DocTypeCForm(request.POST, request.FILES)
        data['formOther'] = DocOtherForm(request.POST, request.FILES)
        # Notary
        data['formNotary'] = NotaryForm(request.POST, request.FILES)
        data['formWR'] = DocWRForm(request.POST, request.FILES)
        data['formDC'] = DocDCForm(request.POST, request.FILES)
        data['formPH'] = DocPHForm(request.POST, request.FILES)
        data['formEs'] = DocEsForm(request.POST, request.FILES)
        # Sii
        data['formSII'] = SII_recordForm(request.POST, request.FILES)
        data['formAc'] = DocAcForm(request.POST, request.FILES)
        data['formDB'] = DocDBForm(request.POST, request.FILES)

        if request.POST.get('Tipo') is not None:
            if request.POST['Tipo'] == 'Propiedad':
                if data['formAcquisition'].is_valid():
                    data['formAcquisition'] = data['formAcquisition'].save(commit=False)
                    if data['formLocation'].is_valid():
                        data['formLocation'] = data['formLocation'].save()
                        aux = Location.objects.get(pk=data['formLocation'].pk)
                        data['formAcquisition'].location = aux
                        data['formAcquisition'].save()
                        return JsonResponse({'id': data['formAcquisition'].pk})

        elif request.POST.get('Arquitecture') is not None:
            if request.POST['Arquitecture'] == 'arquitecture':

                if request.POST.get('id_propiedad') is not None:
                    # extraer pk de la acquisition
                    prop = Acquisition.objects.get(pk=request.POST['id_propiedad'])

                if data['formArquitecture'].is_valid():
                    data['formArquitecture'] = data['formArquitecture'].save(commit=False)
                    if data['formEx'].is_valid():
                        Ex = DocumentEx()
                        if ('ArDocEx' not in request.POST):
                            Ex.archive = request.FILES['ArDocEx']
                        Ex.comment = request.POST['CDocEx']
                        Ex.type = 'EM'
                        Ex.save()
                        data['formArquitecture'].expropriation_mun = Ex
                    if data['formCip'].is_valid():
                        Cip = DocumentCip()
                        if ('ArDocCip' not in request.POST):
                            Cip.archive = request.FILES['ArDocCip']
                        Cip.comment = request.POST['CDocCip']
                        Cip.type = 'CP'
                        Cip.save()
                        data['formArquitecture'].cip = Cip
                    if data['formCn'].is_valid():
                        cn = DocumentCn()
                        if ('ArDocCn' not in request.POST):
                            cn.archive = request.FILES['ArDocCn']
                        cn.comment = request.POST['CDocCn']
                        cn.type = 'NC'
                        cn.save()
                        data['formArquitecture'].certified_number = cn
                    if data['formBlue'].is_valid():
                        blue = DocumentBlue()
                        if ('ArDocBlue' not in request.POST):
                            blue.archive = request.FILES['ArDocBlue']
                        blue.comment = request.POST['CDocBlue']
                        blue.type = 'PL'
                        blue.save()
                        data['formArquitecture'].blueprints = blue
                    if data['formBuildP'].is_valid():
                        build = DocumentBuildP()
                        if ('ArDocBuild' not in request.POST):
                            build.archive = request.FILES['ArDocBuild']
                        build.comment = request.POST['CDocBuild']
                        build.type = 'PE'
                        build.save()
                        data['formArquitecture'].building_permit = build
                    if data['formMR'].is_valid():
                        MR = DocumentMR()
                        if ('ArDocMR' not in request.POST):
                            MR.archive = request.FILES['ArDocMR']
                        MR.type = 'RM'
                        MR.save()
                        data['formArquitecture'].municipal_reception = MR
                    data['formArquitecture'].save()
                    prop.arquitecture = data['formArquitecture']
                    prop.save()
                return JsonResponse({})

        elif request.POST.get('Internal') is not None:
            if request.POST['Internal'] == 'internal':
                if request.POST.get('id_propiedad') is not None:
                    # extraer pk de la acquisition
                    prop = Acquisition.objects.get(pk=request.POST['id_propiedad'])
                if data['formInternal'].is_valid():
                    data['formInternal'] = data['formInternal'].save(commit=False)
                    if data['formTypeC'].is_valid():
                        TypeC = DocumentTypeC()
                        if ('ArDocTypeC' not in request.POST):
                            TypeC.archive = request.FILES['ArDocTypeC']
                        TypeC.comment = request.POST['CDocTypeC']
                        TypeC.type = 'TC'
                        TypeC.save()
                        data['formInternal'].contract_type = TypeC
                    if data['formOther'].is_valid():
                        Other = DocumentOther()
                        if ('ArDocOther' not in request.POST):
                            Other.archive = request.FILES['ArDocOther']
                        Other.comment = request.POST['CDocOther']
                        Other.type = 'OT'
                        Other.save()
                        data['formInternal'].others = Other
                        # guardar en acquisition el intenal
                    data['formInternal'].save()
                    prop.internal = data['formInternal']
                    prop.save()
                    return JsonResponse({})

        elif request.POST.get('Notary') is not None:
            if request.POST['Notary'] == 'notary':
                print('request notary: ',request.POST)
                if request.POST.get('id_propiedad') is not None:
                    # extraer pk de la acquisition
                    prop = Acquisition.objects.get(pk=request.POST['id_propiedad'])

                if data['formNotary'].is_valid():
                    data['formNotary'] = data['formNotary'].save(commit=False)
                    if data['formWR'].is_valid():
                        WR = DocumentWR()
                        if ('ArDocWR' not in request.POST):
                            WR.archive = request.FILES['ArDocWR']
                        WR.comment = request.POST['CDocWR']
                        WR.type = 'ES'
                        WR.save()
                        data['formNotary'].writing = WR
                    if data['formDC'].is_valid():
                        DC = DocumentDC()
                        if ('ArDocDC' not in request.POST):
                            DC.archive = request.FILES['ArDocDC']
                        DC.comment = request.POST['CDocDC']
                        DC.type = 'DC'
                        DC.save()
                        data['formNotary'].domain_certificate = DC
                    if data['formPH'].is_valid():
                        PH = DocumentPH()
                        if ('ArDocPH' not in request.POST):
                            PH.archive = request.FILES['ArDocPH']
                        PH.comment = request.POST['CDocPH']
                        PH.type = 'PR'
                        PH.save()
                        data['formNotary'].prohibitions = PH
                    if data['formDB'].is_valid():
                        Es = DocumentEs()
                        if ('ArDocDB' not in request.POST):
                            Es.archive = request.FILES['ArDocDB']
                        Es.comment = request.POST['CDocDB']
                        Es.type = 'SE'
                        Es.save()
                        data['formNotary'].expropriation_serviu = Es
                    data['formNotary'].save()
                    prop.notary = data['formNotary']
                    prop.save()
                return JsonResponse({})

        elif request.POST.get('SII') is not None:
            if request.POST['SII'] == 'Sii':
                if request.POST.get('id_propiedad') is not None:
                    # extraer pk de la acquisition
                    prop = Acquisition.objects.get(pk=request.POST['id_propiedad'])
                if data['formSII'].is_valid():
                    data['formSII'] = data['formSII'].save(commit=False)
                    if data['formAc'].is_valid():
                        Ac = DocumentAc()
                        if ('ArDocAc' not in request.POST):
                            Ac.archive = request.FILES['ArDocAc']
                        Ac.comment = request.POST['CDocAc']
                        Ac.type = 'CA'
                        Ac.save()
                        data['formSII'].appraisal_certificate = Ac
                    if data['formEs'].is_valid():
                        DB = DocumentDB()
                        if ('ArDocEs' not in request.POST):
                            DB.archive = request.FILES['ArDocEs']
                        DB.comment = request.POST['CDocEs']
                        DB.type = 'CD'
                        DB.save()
                        data['formSII'].debt_certificate = DB
                    data['formSII'].save()
                    prop.SII = data['formSII']
                    prop.save()
                return JsonResponse({})

    else:
        data = {
            'formLocation': LocationForm, 'formAcquisition': AcquisitionForm, 'formArquitecture': ArquitectureForm,
            'formEx': DocExForm, 'formCip': DocCipForm, 'formCn': DocCnForm,
            'formBlue': DocBlueForm,
            'formBuildP': DocBuildPForm, 'formMR': DocMRForm, 'formInternal': InternalForm,
            'formTypeC': DocTypeCForm,
            'formOther': DocOtherForm, 'formNotary': NotaryForm, 'formWR': DocWRForm,
            'formDC': DocDCForm,
            'formPH': DocPHForm, 'formEs': DocEsForm, 'formSII': SII_recordForm,
            'formAc': DocAcForm, 'formDB': DocDBForm,
        }

    return render(request, 'add_acquisition.html', data)


@login_required(login_url='login')
def Add_rent(request):
    data = {}
    if request.method == "POST":
        data['formLocation'] = LocationForm(request.POST)
        data['formRent'] = RentForm(request.POST, request.FILES)
        data['formDocument'] = DocTypeCForm(request.POST, request.FILES)

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
        formDocument = DocTypeCForm()
        formLocation = LocationForm()
        formRent = RentForm()

    return render(request, 'add_rent.html',
                  {'formDocument': formDocument, 'formLocation': formLocation, 'formRent': formRent})


@login_required(login_url='login')
def Edit_acquisition(request, acq_id):

    AcquisitionForm = EditAcquisition(request.POST, request.FILES, instance=Acquisition.objects.get(pk=acq_id))
    data['data'] = EditAcquisition(instance=Acquisition.objects.get(pk=acq_id))

    data = {}
    if request.method == "POST":
        # ArquitectureForm,InternalForm,NotaryForm,SII_recordForm
        data['formAcquisition'] = AcquisitionForm(request.POST, request.FILES)
        data['formLocation'] = LocationForm(request.POST, request.FILES)
        # Arquitecture
        data['formArquitecture'] = ArquitectureForm(request.POST, request.FILES)
        data['formEx'] = DocExForm(request.POST, request.FILES)
        data['formCip'] = DocCipForm(request.POST, request.FILES)
        data['formCn'] = DocCnForm(request.POST, request.FILES)
        data['formBlue'] = DocBlueForm(request.POST, request.FILES)
        data['formBuildP'] = DocBuildPForm(request.POST, request.FILES)
        data['formMR'] = DocMRForm(request.POST, request.FILES)
        # Internal
        data['formInternal'] = InternalForm(request.POST, request.FILES)
        data['formTypeC'] = DocTypeCForm(request.POST, request.FILES)
        data['formOther'] = DocOtherForm(request.POST, request.FILES)
        # Notary
        data['formNotary'] = NotaryForm(request.POST, request.FILES)
        data['formWR'] = DocWRForm(request.POST, request.FILES)
        data['formDC'] = DocDCForm(request.POST, request.FILES)
        data['formPH'] = DocPHForm(request.POST, request.FILES)
        data['formEs'] = DocEsForm(request.POST, request.FILES)
        # Sii
        data['formSII'] = SII_recordForm(request.POST, request.FILES)
        data['formAc'] = DocAcForm(request.POST, request.FILES)
        data['formDB'] = DocDBForm(request.POST, request.FILES)

        if request.POST.get('Tipo') is not None:
            if request.POST['Tipo'] == 'Propiedad':
                if data['formAcquisition'].is_valid():
                    data['formAcquisition'] = data['formAcquisition'].save(commit=False)
                    if data['formLocation'].is_valid():
                        data['formLocation'] = data['formLocation'].save()
                        aux = Location.objects.get(pk=data['formLocation'].pk)
                        data['formAcquisition'].location = aux
                        data['formAcquisition'].save()
                        return JsonResponse({'id': data['formAcquisition'].pk})

        elif request.POST.get('Arquitecture') is not None:
            if request.POST['Arquitecture'] == 'arquitecture':
                if data['formArquitecture'].is_valid():
                    data['formArquitecture'] = data['formArquitecture'].save(commit=False)
                    if data['formEx'].is_valid():
                        Ex = DocumentEx()
                        if ('ArDocEx' not in request.POST):
                            Ex.archive = request.FILES['ArDocEx']
                        Ex.comment = request.POST['CDocEx']
                        Ex.type = 'EM'
                        Ex.save()
                        data['formArquitecture'].expropriation_mun = Ex
                    if data['formCip'].is_valid():
                        Cip = DocumentCip()
                        if ('ArDocCip' not in request.POST):
                            Cip.archive = request.FILES['ArDocCip']
                        Cip.comment = request.POST['CDocCip']
                        Cip.type = 'CP'
                        Cip.save()
                        data['formArquitecture'].cip = Cip
                    if data['formCn'].is_valid():
                        cn = DocumentCn()
                        if ('ArDocCn' not in request.POST):
                            cn.archive = request.FILES['ArDocCn']
                        cn.comment = request.POST['CDocCn']
                        cn.type = 'NC'
                        cn.save()
                        data['formArquitecture'].certified_number = cn
                    if data['formBlue'].is_valid():
                        blue = DocumentBlue()
                        if ('ArDocBlue' not in request.POST):
                            blue.archive = request.FILES['ArDocBlue']
                        blue.comment = request.POST['CDocBlue']
                        blue.type = 'PL'
                        blue.save()
                        data['formArquitecture'].blueprints = blue
                    if data['formBuildP'].is_valid():
                        build = DocumentBuildP()
                        if ('ArDocBuild' not in request.POST):
                            build.archive = request.FILES['ArDocBuild']
                        build.comment = request.POST['CDocBuild']
                        build.type = 'PE'
                        build.save()
                        data['formArquitecture'].building_permit = build
                    if data['formMR'].is_valid():
                        MR = DocumentMR()
                        if ('ArDocMR' not in request.POST):
                            MR.archive = request.FILES['ArDocMR']
                        MR.type = 'RM'
                        MR.save()
                        data['formArquitecture'].municipal_reception = MR
                    data['formArquitecture'].save()
                return JsonResponse({})

        elif request.POST.get('Internal') is not None:
            if request.POST['Internal'] == 'internal':
                if data['formInternal'].is_valid():
                    data['formInternal'] = data['formInternal'].save(commit=False)
                    if data['formTypeC'].is_valid():
                        TypeC = DocumentTypeC()
                        if ('ArDocTypeC' not in request.POST):
                            TypeC.archive = request.FILES['ArDocTypeC']
                        TypeC.comment = request.POST['CDocTypeC']
                        TypeC.type = 'TC'
                        TypeC.save()
                        data['formInternal'].contract_type = TypeC
                    if data['formOther'].is_valid():
                        Other = DocumentOther()
                        if ('ArDocOther' not in request.POST):
                            Other.archive = request.FILES['ArDocOther']
                        Other.comment = request.POST['CDocOther']
                        Other.type = 'OT'
                        Other.save()
                        data['formInternal'].others = Other
                    data['formInternal'].save()
                    # guardar en acquisition el intenal
                    return JsonResponse({})

        elif request.POST.get('Notary') is not None:
            if request.POST['Notary'] == 'notary':
                if data['formNotary'].is_valid():
                    data['formNotary'] = data['formNotary'].save(commit=False)
                    if data['formWR'].is_valid():
                        WR = DocumentWR()
                        if ('ArDocWR' not in request.POST):
                            WR.archive = request.FILES['ArDocWR']
                        WR.comment = request.POST['CDocWR']
                        WR.type = 'ES'
                        WR.save()
                        data['formNotary'].writing = WR
                    if data['formDC'].is_valid():
                        DC = DocumentDC()
                        if ('ArDocDC' not in request.POST):
                            DC.archive = request.FILES['ArDocDC']
                        DC.comment = request.POST['CDocDC']
                        DC.type = 'DC'
                        DC.save()
                        data['formNotary'].domain_certificate = DC
                    if data['formPH'].is_valid():
                        PH = DocumentPH()
                        if ('ArDocPH' not in request.POST):
                            PH.archive = request.FILES['ArDocPH']
                        PH.comment = request.POST['CDocPH']
                        PH.type = 'PR'
                        PH.save()
                        data['formNotary'].prohibitions = PH
                    if data['formEs'].is_valid():
                        Es = DocumentEs()
                        if ('ArDocEs' not in request.POST):
                            Es.archive = request.FILES['ArDocEs']
                        Es.comment = request.POST['CDocEs']
                        Es.type = 'SE'
                        Es.save()
                        data['formNotary'].expropriation_serviu = Es
                    data['formNotary'].save()
                return JsonResponse({})

        elif request.POST.get('SII') is not None:
            if request.POST['SII'] == 'Sii':
                if data['formSII'].is_valid():
                    data['formSII'] = data['formSII'].save(commit=False)
                    if data['formAc'].is_valid():
                        Ac = DocumentAc()
                        if ('ArDocAc' not in request.POST):
                            Ac.archive = request.FILES['ArDocAc']
                        Ac.comment = request.POST['CDocAc']
                        Ac.type = 'CA'
                        Ac.save()
                        data['formSII'].appraisal_certificate = Ac
                    if data['formDB'].is_valid():
                        DB = DocumentDB()
                        if ('ArDocDB' not in request.POST):
                            DB.archive = request.FILES['ArDocDB']
                        DB.comment = request.POST['CDocDB']
                        DB.type = 'CD'
                        DB.save()
                        data['formSII'].debt_certificate = DB
                    data['formSII'].save()
                return JsonResponse({})

    else:
        data = {
            'formLocation': LocationForm, 'formAcquisition': AcquisitionForm, 'formArquitecture': ArquitectureForm,
            'formEx': DocExForm, 'formCip': DocCipForm, 'formCn': DocCnForm,
            'formBlue': DocBlueForm,
            'formBuildP': DocBuildPForm, 'formMR': DocMRForm, 'formInternal': InternalForm,
            'formTypeC': DocTypeCForm,
            'formOther': DocOtherForm, 'formNotary': NotaryForm, 'formWR': DocWRForm,
            'formDC': DocDCForm,
            'formPH': DocPHForm, 'formEs': DocEsForm, 'formSII': SII_recordForm,
            'formAc': DocAcForm, 'formDB': DocDBForm,
        }

    return render(request, 'add_acquisition.html', data)


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
def view_archive(request, document_type, document_id):
    data = {}
    data['request'] = request
    template_name = 'view_archive.html'
    if document_type == 'EM':
        if document_id != None:
            data['archive'] = DocumentEx.objects.get(pk=document_id)
            return render(request, template_name, data)
        else:
            return render(request, template_name)
    elif document_type == 'CP':
        if document_id != None:
            data['archive'] = DocumentCip.objects.get(pk=document_id)
            return render(request, template_name, data)
        else:
            return render(request, template_name)
    elif document_type == 'NC':
        if document_id != None:
            data['archive'] = DocumentCn.objects.get(pk=document_id)
            return render(request, template_name, data)
        else:
            return render(request, template_name)
    elif document_type == 'PL':
        if document_id != None:
            data['archive'] = DocumentBlue.objects.get(pk=document_id)
            return render(request, template_name, data)
        else:
            return render(request, template_name)
    elif document_type == 'PE':
        if document_id != None:
            data['archive'] = DocumentBuildP.objects.get(pk=document_id)
            return render(request, template_name, data)
        else:
            return render(request, template_name)
    elif document_type == 'RM':
        if document_id != None:
            data['archive'] = DocumentMR.objects.get(pk=document_id)
            return render(request, template_name, data)
        else:
            return render(request, template_name)
    elif document_type == 'TC':
        if document_id != None:
            data['archive'] = DocumentTypeC.objects.get(pk=document_id)
            return render(request, template_name, data)
        else:
            return render(request, template_name)
    elif document_type == 'OT':
        if document_id != None:
            data['archive'] = DocumentOther.objects.get(pk=document_id)
            return render(request, template_name, data)
        else:
            return render(request, template_name)
    elif document_type == 'ES':
        if document_id != None:
            data['archive'] = DocumentWR.objects.get(pk=document_id)
            return render(request, template_name, data)
        else:
            return render(request, template_name)
    elif document_type == 'DC':
        if document_id != None:
            data['archive'] = DocumentDC.objects.get(pk=document_id)
            return render(request, template_name, data)
        else:
            return render(request, template_name)
    elif document_type == 'SE':
        if document_id != None:
            data['archive'] = DocumentEs.objects.get(pk=document_id)
            return render(request, template_name, data)
        else:
            return render(request, template_name)
    elif document_type == 'CA':
        if document_id != None:
            data['archive'] = DocumentAc.objects.get(pk=document_id)
            return render(request, template_name, data)
        else:
            return render(request, template_name)
    elif document_type == 'CD':
        if document_id != None:
            data['archive'] = DocumentDB.objects.get(pk=document_id)
            return render(request, template_name, data)
        else:
            return render(request, template_name)
    elif document_type == 'PR':
        if document_id != None:
            data['archive'] = DocumentPH.objects.get(pk=document_id)
            return render(request, template_name, data)
        else:
            return render(request, template_name)
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

@login_required(login_url='login')
def search(request):
    template = 'search.html'
    data = {}
    data[request] = request
    query = request.GET.get('q')
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