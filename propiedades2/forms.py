# -*- coding: utf-8 -*-
from django.forms import ModelForm
from propiedades2.models import Location, Acquisition, Document, \
    ArchitectureRecordAcq, InternalAccountantsAcq, NotaryAcquisition, SiiRecord,Rent,Post
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ['archive','comment', ]
        labels = {
            'archive': 'Archivo',
            'comment': 'Comentario',
        }
        widgets = {
            'archive': forms.FileInput(attrs={'class': 'form-control','id': 'doccip'}),
            'comment': forms.TextInput(attrs={'class': 'form-control'}),
        }

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['street', 'number', 'commune', 'city', 'region', 'plot', 'lot_number']
        labels = {
            'street': 'Nombre Calle',
            'number': 'Número',
            'commune': 'Comuna',
            'city': 'Ciudad',
            'region': 'Región',
            'plot': 'Parcela',
            'lot_number': 'Número de parcela'
        }
        widgets = {
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
            'commune': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'lot_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'plot': forms.TextInput(attrs={'class': 'form-control'})
        }


class AcquisitionForm(ModelForm):
    class Meta:
        model = Acquisition
        fields = ['name', 'role_number', 'image', 'property_use', 'acquisition_date', 'writing_data', 'number_AASI', ]

        labels = {'name': 'Nombre',
                  'role_number': 'Número de rol',
                  'image': 'Imagen',
                  'property_use': 'Uso de la propiedad',
                  'number_AASI': 'Número AASI.net',
                  'acquisition_date': 'Fecha de adquisición',
                  'writing_data': 'Datos de escritura',
                  }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'role_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'property_use': forms.Select(attrs={'class': 'form-control'}),
            'number_AASI': forms.NumberInput(attrs={'class': 'form-control'}),
            'acquisition_date': forms.DateTimeInput(attrs={'class': 'form-control', 'id': 'id_acquisition_date'}),
            'writing_data': forms.Select(attrs={'class': 'form-control'}),
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
            'ground_surface': forms.TextInput(attrs={'class': 'form-control'}),
            'square_m_build': forms.TextInput(attrs={'class': 'form-control'}),
            'e_construction_m': forms.TextInput(attrs={'class': 'form-control'}),
            'municipal_n': forms.NumberInput(attrs={'class': 'form-control'}),
            'n_building_permit': forms.NumberInput(attrs={'class': 'form-control'}),
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
            'value_land': forms.NumberInput(attrs={'class': 'form-control'}),
            'value_construction': forms.NumberInput(attrs={'class': 'form-control'}),
            'acquiring_name': forms.TextInput(attrs={'class': 'form-control'}),
            'supplier_name': forms.TextInput(attrs={'class': 'form-control'}),
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
            'notary': forms.TextInput(attrs={'class': 'form-control'}),
            'writing_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'sale_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'previous_title': forms.TextInput(attrs={'class': 'form-control'}),
            'current_title': forms.TextInput(attrs={'class': 'form-control'}),
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
            'destiny': forms.TextInput(attrs={'class': 'form-control'}),
            'tax_appraisal': forms.NumberInput(attrs={'class': 'form-control'}),
            'owner_name_SII': forms.TextInput(attrs={'class': 'form-control'}),
            'total_debt': forms.NumberInput(attrs={'class': 'form-control'}),
            'ex_contributions': forms.CheckboxInput(attrs={'class': 'form-control'}),
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
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'role_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'property_use': forms.Select(attrs={'class': 'form-control'}),
            'ground_surface': forms.TextInput(attrs={'class': 'form-control'}),
            'square_m_build': forms.TextInput(attrs={'class': 'form-control'}),
            'e_construction_m': forms.TextInput(attrs={'class': 'form-control'}),
            'municipal_n': forms.NumberInput(attrs={'class': 'form-control'}),
            'n_building_permit': forms.NumberInput(attrs={'class': 'form-control'}),
            'value_land': forms.TextInput(attrs={'class': 'form-control'}),
            'value_construction': forms.TextInput(attrs={'class': 'form-control'}),
            'acquiring_name': forms.TextInput(attrs={'class': 'form-control'}),
            'supplier_name': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    class PostForm(ModelForm):
        class Meta:
            model = Post
            fields = ['title', 'description', 'author', 'publish_date', 'acquisition', 'rent', ]
