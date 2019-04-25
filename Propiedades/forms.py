# -*- coding: utf-8 -*-
from django.forms import ModelForm
from Propiedades.models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DocumentForm(ModelForm):

    class Meta:
        model = Document
        fields = ['archive','publish_date','comment',]

class LocationForm(ModelForm):

    class Meta:
        model = Location
        fields = ['street','number','commune','city','region','lot_number','plot',]

class AcquisitionForm(ModelForm):

    class Meta:
        model = Acquisition
        fields = ['name','role_number','image','property_use','location','ground_surface','square_m_build','e_construction_m','municipal_n','n_building_permit','value_land','value_construction',
                  'number_AASI','acquisition_date','contract_type','acquiring_name','supplier_name','writing_data','notary','writing_year','sale_price','previous_title','current_title',
                  'destiny','tax_appraisal','owner_name_SII','total_debt','ex_contributions','writing','domain_certificate','prohibitions','expropriation_serviu','others','expropriation_mun',
                  'cip','certified_number','blueprints','building_permit','municipal_reception','appraisal_certificate','debt_certificate',]

        labels = {'name' : 'Nombre',
                  'role_number' : 'Número de rol',
                  'image' : 'Imagen',
                  'property_use' : 'Uso de la propiedad',
                  'location' : 'Dirección',
                  'ground_surface' : 'Superficie de terreno',
                  'square_m_build' : 'Metros cuadrados construidos PE-RF',
                  'e_construction_m' : 'Metros construción existente',
                  'municipal_n' : 'Número de recepción municipal',
                  'n_building_permit' : 'Número de permiso de edificación',
                  'number_AASI': 'Número AASI.net',
                  'acquisition_date': 'Fecha de adquisición',
                  'contract_type': 'Tipo de contrato',
                  'acquiring_name': 'Nombre de comprador o donador',
                  'supplier_name' : 'Nombre de vendedor o donatario',
                  'writing_data' : 'Datos de escritura',
                  'notary' : 'Notaría',
                  'writing_year': 'Año de escritura',
                  'sale_price' : 'Precio de venta',
                  'previous_title' : 'Titulo anterior',
                  'current_title' : 'Titulo actual',
                  'destiny' : 'Destino SII',
                  'tax_appraisal' : 'Avalúo fiscal',
                  'owner_name_SII' : 'Nombre de propietario SII',
                  'total_debt' : 'Deuda total',
                  'ex_contributions' : 'Exención de contribuciones',
                  'writing': 'Documento de escritura',
                  'domain_certificate' : 'Certificado de dominio',
                  'prohibitions' : 'Gravamenes y prohibiciones',
                  'expropriation_serviu' : 'Documento no expropiación SERVIU',
                  'others' : 'Otros',
                  'expropriation_mun': 'Documento no expropiación Municipal',
                  'cip': 'Documento CIP',
                  'certified_number' : 'Certificado número',
                  'blueprints':'Planos',
                  'building_permit': 'Permiso de edificación',
                  'municipal_reception': 'Recepción municipal',
                  'appraisal_certificate':'Certificado de avalúo',
                  'debt_certificate':'Certificado de no deuda'
        }

class RentForm(ModelForm):

    class Meta:
        model = Rent
        fields = ['name','role_number','image','property_use','location','ground_surface','square_m_build',
                  'e_construction_m','municipal_n','n_building_permit','value_land','value_construction','contract_type',
                  'acquiring_name','supplier_name','start_date','end_date','duration',]
        labels = {
            'name' : 'Nombre',
            'role_number' : 'Número de rol',
            'image' : 'Imagen',
            'property_use' : 'Uso de la propiedad',
            'location' : 'Dirección',
            'ground_surface' : 'Superficie de terreno',
            'square_m_build' : 'Metros cuadrados construidos PE-RF',
            'e_construction_m' : 'Metros construción existente',
            'municipal_n' : 'Número de recepción municipal',
            'n_building_permit' : 'Número de permiso de edificación',
            'contract_type' : 'Tipo de contrato',
            'acquiring_name' : 'Nombre de arrendatario',
            'supplier_name' : 'Nombre del arrendador',
            'start_date' : 'Fecha de comienzo del contrato',
            'end_date' : 'Fecha de finalización del contrato',
            'duration' : 'Duración del contrato',
        }

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title','description','author','publish_date','acquisition','rent',]