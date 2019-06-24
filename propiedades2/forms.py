# -*- coding: utf-8 -*-
from django.forms import ModelForm
from propiedades2.models import Location, Acquisition, DocumentEx, DocumentCip, DocumentCn, DocumentBlue, \
    DocumentBuildP, DocumentMR, DocumentTypeC, DocumentOther, DocumentWR, DocumentDC, DocumentPH, DocumentDB, \
    DocumentAc, DocumentEs, ArchitectureRecordAcq, InternalAccountantsAcq, NotaryAcquisition, SiiRecord, Rent, Post
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Documentos de arquitectura
class DocExForm(ModelForm):
    class Meta:
        model = DocumentEx
        fields = ['archive', 'comment', ]
        labels = {
            'archive': 'Archivo',
            'comment': 'Comentario',
        }
        widgets = {
            'archive': forms.FileInput(attrs={'class': 'form-control', 'type': 'file', 'id': 'docEx'}),
            'comment': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese un comentario', 'id': 'CdocEx'}),
        }


class DocCipForm(ModelForm):
    class Meta:
        model = DocumentCip
        fields = ['archive', 'comment', ]
        labels = {
            'archive': 'Archivo',
            'comment': 'Comentario',
        }
        widgets = {
            'archive': forms.FileInput(attrs={'class': 'form-control', 'type': 'file', 'id': 'docCip'}),
            'comment': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese un comentario', 'id': 'CdocCip'}),
        }


class DocCnForm(ModelForm):
    class Meta:
        model = DocumentCn
        fields = ['archive', 'comment', ]
        labels = {
            'archive': 'Archivo',
            'comment': 'Comentario',
        }
        widgets = {
            'archive': forms.FileInput(attrs={'class': 'form-control', 'type': 'file', 'id': 'docCn'}),
            'comment': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese un comentario', 'id': 'CdocCn'}),
        }


class DocBlueForm(ModelForm):
    class Meta:
        model = DocumentBlue
        fields = ['archive', 'comment', ]
        labels = {
            'archive': 'Archivo',
            'comment': 'Comentario',
        }
        widgets = {
            'archive': forms.FileInput(attrs={'class': 'form-control', 'type': 'file', 'id': 'docBlue'}),
            'comment': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese un comentario', 'id': 'CdocBlue'}),
        }


class DocBuildPForm(ModelForm):
    class Meta:
        model = DocumentBuildP
        fields = ['archive', 'comment', ]
        labels = {
            'archive': 'Archivo',
            'comment': 'Comentario',
        }
        widgets = {
            'archive': forms.FileInput(attrs={'class': 'form-control', 'type': 'file', 'id': 'docBuild'}),
            'comment': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese un comentario', 'id': 'CdocBuild'}),
        }


class DocMRForm(ModelForm):
    class Meta:
        model = DocumentMR
        fields = ['archive', 'comment', ]
        labels = {
            'archive': 'Archivo',
            'comment': 'Comentario',
        }
        widgets = {
            'archive': forms.FileInput(attrs={'class': 'form-control', 'type': 'file', 'id': 'docMR'}),
            'comment': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese un comentario', 'id': 'CdocMR'}),
        }

#Documentos internos

class DocTypeCForm(ModelForm):
    class Meta:
        model = DocumentTypeC
        fields = ['archive', 'comment', ]
        labels = {
            'archive': 'Archivo',
            'comment': 'Comentario',
        }
        widgets = {
            'archive': forms.FileInput(attrs={'class': 'form-control', 'type': 'file', 'id': 'docTypeC'}),
            'comment': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese un comentario', 'id': 'CdocTypeC'}),
        }


class DocOtherForm(ModelForm):
    class Meta:
        model = DocumentOther
        fields = ['archive', 'comment', ]
        labels = {
            'archive': 'Archivo',
            'comment': 'Comentario',
        }
        widgets = {
            'archive': forms.FileInput(attrs={'class': 'form-control', 'type': 'file', 'id': 'docOther'}),
            'comment': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese un comentario', 'id': 'CdocOther'}),
        }

#Documentos de notaria

class DocWRForm(ModelForm):
    class Meta:
        model = DocumentWR
        fields = ['archive', 'comment', ]
        labels = {
            'archive': 'Archivo',
            'comment': 'Comentario',
        }
        widgets = {
            'archive': forms.FileInput(attrs={'class': 'form-control', 'type': 'file', 'id': 'docWR'}),
            'comment': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese un comentario', 'id': 'CdocWR'}),
        }


class DocDCForm(ModelForm):
    class Meta:
        model = DocumentDC
        fields = ['archive', 'comment', ]
        labels = {
            'archive': 'Archivo',
            'comment': 'Comentario',
        }
        widgets = {
            'archive': forms.FileInput(attrs={'class': 'form-control', 'type': 'file', 'id': 'docDC'}),
            'comment': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese un comentario', 'id': 'CdocDC'}),
        }


class DocPHForm(ModelForm):
    class Meta:
        model = DocumentPH
        fields = ['archive', 'comment', ]
        labels = {
            'archive': 'Archivo',
            'comment': 'Comentario',
        }
        widgets = {
            'archive': forms.FileInput(attrs={'class': 'form-control', 'type': 'file', 'id': 'docPH'}),
            'comment': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese un comentario', 'id': 'CdocPH'}),
        }


class DocDBForm(ModelForm):
    class Meta:
        model = DocumentDB
        fields = ['archive', 'comment', ]
        labels = {
            'archive': 'Archivo',
            'comment': 'Comentario',
        }
        widgets = {
            'archive': forms.FileInput(attrs={'class': 'form-control', 'type': 'file', 'id': 'docDB'}),
            'comment': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese un comentario', 'id': 'CdocDB'}),
        }

#Documentos de SII
class DocAcForm(ModelForm):
    class Meta:
        model = DocumentAc
        fields = ['archive', 'comment', ]
        labels = {
            'archive': 'Archivo',
            'comment': 'Comentario',
        }
        widgets = {
            'archive': forms.FileInput(attrs={'class': 'form-control', 'type': 'file', 'id': 'docAc'}),
            'comment': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese un comentario', 'id': 'CdocAc'}),
        }


class DocEsForm(ModelForm):
    class Meta:
        model = DocumentEs
        fields = ['archive', 'comment', ]
        labels = {
            'archive': 'Archivo',
            'comment': 'Comentario',
        }
        widgets = {
            'archive': forms.FileInput(attrs={'class': 'form-control', 'type': 'file', 'id': 'docEs'}),
            'comment': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese un comentario', 'id': 'CdocEs'}),
        }


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['street', 'number', 'commune', 'city', 'region', 'plot', 'lot_number']
        labels = {
            'street': 'Nombre Calle*',
            'number': 'Número*',
            'commune': 'Comuna*',
            'city': 'Ciudad*',
            'region': 'Región*',
            'plot': 'Parcela',
            'lot_number': 'Número de parcela'
        }
        widgets = {
            'street': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre de la calle', 'id': 'street'}),
            'number': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese número de la propiedad', 'id': 'number'}),
            'commune': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre de la comuna', 'id': 'commune'}),
            'city': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre de la ciudad', 'id': 'city'}),
            'region': forms.Select(attrs={'class': 'form-control', 'id': 'region'}),
            'lot_number': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese número de la parcela', 'id': 'lot_number'}),
            'plot': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre de parcela', 'id': 'plot'})
        }


class AcquisitionForm(ModelForm):
    class Meta:
        model = Acquisition
        fields = ['name', 'role_number', 'image', 'property_use', 'acquisition_date', 'writing_data', 'number_AASI', ]

        labels = {'name': 'Nombre*',
                  'role_number': 'Número de rol*',
                  'image': 'Imagen',
                  'property_use': 'Uso de la propiedad*',
                  'number_AASI': 'Número AASI.net*',
                  'acquisition_date': 'Fecha de adquisición*',
                  'writing_data': 'Datos de escritura*',
                  }

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre de la propiedad', 'id': 'name'}),
            'role_number': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese número de rol', 'id': 'role_number'}),
            'image': forms.FileInput(
                attrs={'class': 'form-control', 'placeholder': 'Seleccione una imagen', 'id': 'image', 'type': 'file'}),
            'property_use': forms.Select(attrs={'class': 'form-control', 'id': 'property_use'}),
            'number_AASI': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese número de AASI.net', 'id': 'number_AASI'}),
            'acquisition_date': forms.DateInput(
                attrs={'class': 'form-control', 'id': 'acquisition_date', 'placeholder': 'Ingrese fecha de adquisición',
                       'type': 'date'}),
            'writing_data': forms.Select(attrs={'class': 'form-control', 'id': 'writing_data'}),
        }


class ArquitectureForm(ModelForm):
    class Meta:
        model = ArchitectureRecordAcq
        fields = [
            'ground_surface', 'square_m_build', 'e_construction_m', 'municipal_n', 'n_building_permit',
        ]

        labels = {
            'ground_surface': 'Superficie de terreno',
            'square_m_build': 'Metros cuadrados construidos PE-RF',
            'e_construction_m': 'Metros construcción existente',
            'municipal_n': 'Número de recepción municipal',
            'n_building_permit': 'Número de permiso de edificación'
        }

        widgets = {
            'ground_surface': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese superficie',
                       'id': 'ground_surface'}),
            'square_m_build': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese metros cuadrados',
                       'id': 'square_m_build'}),
            'e_construction_m': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese metros cuadrados',
                       'id': 'e_construction_m'}),
            'municipal_n': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese número',
                       'id': 'municipal_n'}),
            'n_building_permit': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese número de permiso de edificación',
                       'id': 'n_building_permit'}),
        }


class InternalForm(ModelForm):
    class Meta:
        model = InternalAccountantsAcq
        fields = [
            'value_land', 'value_construction', 'acquiring_name', 'supplier_name',
        ]

        labels = {
            'value_land': 'Valor del terreno',
            'value_construction': 'Valor de la construcción',
            'acquiring_name': 'Nombre de comprador o donador',
            'supplier_name': 'Nombre de vendedor o donatario',
        }

        widgets = {
            'value_land': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese valor del terreno', 'id': 'value_land'}),
            'value_construction': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese valor construcción',
                       'id': 'value_construction'}),
            'acquiring_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre del comprador o donador',
                       'id': 'acquiring_name'}),
            'supplier_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre del vendedor o donatario',
                       'id': 'supplier_name'}),
        }


class NotaryForm(ModelForm):
    class Meta:
        model = NotaryAcquisition
        fields = [
            'notary', 'writing_year', 'sale_price', 'previous_title', 'current_title', ]

        labels = {
            'notary': 'Notaría',
            'writing_year': 'Año de escritura',
            'sale_price': 'Precio de venta',
            'previous_title': 'Titulo anterior',
            'current_title': 'Titulo actual',
        }

        widgets = {
            'notary': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre de la notaría', 'id': 'notary'}),
            'writing_year': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese el año de escritura', 'id': 'writing_year'}),
            'sale_price': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese el precio de venta de la propiedad',
                       'id': 'sale_price'}),
            'previous_title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese el título anterior', 'id': 'previous_title'}),
            'current_title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese el título actual', 'id': 'current_title'}),
        }


class SII_recordForm(ModelForm):
    class Meta:
        model = SiiRecord
        fields = [
            'destiny', 'tax_appraisal', 'owner_name_SII', 'total_debt', 'ex_contributions', ]

        labels = {
            'destiny': 'Destino SII',
            'tax_appraisal': 'Avalúo fiscal',
            'owner_name_SII': 'Nombre de propietario SII',
            'total_debt': 'Deuda total',
            'ex_contributions': 'Exención de contribuciones',
        }

        widgets = {
            'destiny': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese destino de SII', 'id': 'destiny'}),
            'tax_appraisal': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese el avalúo fiscal', 'id': 'tax_appraisal'}),
            'owner_name_SII': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre del propietario en SII',
                       'id': 'owner_name_SII'}),
            'total_debt': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese deuda total', 'id': 'total_debt'}),
            'ex_contributions': forms.CheckboxInput(attrs={'class': 'form-control', 'id': 'ex_contributions'}),
        }


class RentForm(ModelForm):
    class Meta:
        model = Rent
        fields = ['name', 'role_number', 'image', 'property_use', 'ground_surface', 'square_m_build',
                  'e_construction_m', 'municipal_n', 'n_building_permit', 'value_land', 'value_construction',
                  'acquiring_name', 'supplier_name', 'start_date', 'end_date', 'duration', ]
        labels = {
            'name': 'Nombre',
            'role_number': 'Número de rol',
            'image': 'Imagen',
            'property_use': 'Uso de la propiedad',
            'ground_surface': 'Superficie de terreno',
            'square_m_build': 'Metros cuadrados construidos PE-RF',
            'e_construction_m': 'Metros construcción existente',
            'municipal_n': 'Número de recepción municipal',
            'n_building_permit': 'Número de permiso de edificación',
            'value_land': 'Valor del terreno',
            'value_construction': 'Valor de la construcción',
            'acquiring_name': 'Nombre de arrendatario',
            'supplier_name': 'Nombre del arrendador',
            'start_date': 'Fecha de comienzo del contrato',
            'end_date': 'Fecha de finalización del contrato',
            'duration': 'Duración del contrato',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre de la propiedad'}),
            'role_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese número de rol'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'property_use': forms.Select(attrs={'class': 'form-control'}),
            'ground_surface': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese superficie del terreno'}),
            'square_m_build': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese metros cuadrados construidos'}),
            'e_construction_m': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese metros cuadrados de construcción existente'}),
            'municipal_n': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese número de recepción municipal'}),
            'n_building_permit': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese número de permiso de edificación'}),
            'value_land': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese valor del terreno'}),
            'value_construction': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese valor de la construcción'}),
            'acquiring_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre del arrendatario'}),
            'supplier_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre del arrendador'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'duration': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese fecha de duración del contrato'}),
        }

    class PostForm(ModelForm):
        class Meta:
            model = Post
            fields = ['title', 'description', 'author', 'publish_date', 'acquisition', 'rent', ]
