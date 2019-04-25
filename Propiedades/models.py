# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from Propiedades.defines import *
from Auth_users.models import UserProfile
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Document(models.Model):
    archive = models.FileField(upload_to='Documentos/', blank=True, null=True)
    publish_date = models.DateTimeField(default=timezone.now)
    comment = models.CharField(max_length=300)

class Location(models.Model):
    street = models.CharField(max_length=200)
    number = models.PositiveIntegerField()
    commune = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=200, choices=REGION_CHOICE)
    lot_number = models.PositiveIntegerField(blank=True, null=True)
    plot = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return "calle: %s %s" % (self.street, self.number)


class Acquisition(models.Model):
    name = models.CharField(max_length=200)
    role_number = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='Fotos/',blank=True, null=True)
    property_use = models.CharField(max_length=100,choices=PROPERTY_USE_CHOICE)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    #antecedentes de arquitectura
    ground_surface = models.CharField(max_length=100,blank=True, null=True)
    square_m_build = models.CharField(max_length=100,blank=True, null=True)
    e_construction_m = models.CharField(max_length=100,blank=True, null=True)
    municipal_n = models.PositiveIntegerField(blank=True, null=True)
    n_building_permit = models.PositiveIntegerField(blank=True, null=True)
    #contables internos
    value_land = models.CharField(max_length=100,blank=True, null=True)
    value_construction = models.CharField(max_length=100,blank=True, null=True)
    number_AASI = models.PositiveIntegerField(blank=True, null=True)
    acquisition_date = models.DateField(default=timezone.now)
    contract_type = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='TipoContratoAdquisicion')
    acquiring_name = models.CharField(max_length=100,blank=True, null=True)
    supplier_name = models.CharField(max_length=100,blank=True, null=True)
    writing_data = models.CharField(max_length=100,choices=WRITING_DATA_CHOICE)
    #notaria
    notary = models.CharField(max_length=100,blank=True, null=True)
    writing_year = models.PositiveIntegerField(blank=True, null=True)
    sale_price = models.CharField(max_length=100,blank=True, null=True)
    #antecedentes de dominio
    previous_title = models.CharField(max_length=100,blank=True, null=True)
    current_title = models.CharField(max_length=100,blank=True, null=True)
    #antecendentes impuestos internos
    destiny = models.CharField(max_length=100,blank=True, null=True)
    tax_appraisal = models.PositiveIntegerField(blank=True, null=True)
    owner_name_SII = models.CharField(max_length=100,blank=True, null=True)
    total_debt = models.PositiveIntegerField(blank=True, null=True)
    ex_contributions = models.NullBooleanField()
    writing = models.ForeignKey(Document, on_delete=models.CASCADE, blank=True, null=True, related_name='Escritura')
    domain_certificate = models.ForeignKey(Document, on_delete=models.CASCADE, null=True, blank=True,related_name='CertificadoDominio')
    prohibitions = models.ForeignKey(Document, on_delete=models.CASCADE, blank=True, null=True, related_name='Prohibiciones')
    expropriation_serviu = models.ForeignKey(Document, on_delete=models.CASCADE, blank=True, null=True, related_name='Serviu')
    others = models.ForeignKey(Document, on_delete=models.CASCADE, blank=True, null=True, related_name='Otros')
    # arquitectura y municipales
    expropriation_mun = models.ForeignKey(Document, on_delete=models.CASCADE, blank=True, null=True,related_name='ExMunicipalidad')
    cip = models.ForeignKey(Document, on_delete=models.CASCADE, blank=True, null=True, related_name='Cip')
    certified_number = models.ForeignKey(Document, on_delete=models.CASCADE, blank=True, null=True,related_name='NumCertificado')
    blueprints = models.ForeignKey(Document, on_delete=models.CASCADE, blank=True, null=True, related_name='Planos')
    building_permit = models.ForeignKey(Document, on_delete=models.CASCADE, blank=True, null=True,related_name='PerEdificacion')
    municipal_reception = models.ForeignKey(Document, on_delete=models.CASCADE, blank=True, null=True,related_name='RecMunicipal')
    # SII - TGR
    appraisal_certificate = models.ForeignKey(Document, on_delete=models.CASCADE, blank=True, null=True,related_name='CerAvaluo')
    debt_certificate = models.ForeignKey(Document, on_delete=models.CASCADE, blank=True, null=True,related_name='CerNoDeuda')

    def __str__(self):
        return "nombre: %s, rol: %s, uso: %s" % (self.name, self.role_number, self.property_use)

class Rent(models.Model):
    name = models.CharField(max_length=200)
    role_number = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='Fotos/',blank=True, null=True)
    property_use = models.CharField(max_length=100,choices=PROPERTY_USE_CHOICE)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    #antecedentes de arquitectura
    ground_surface = models.CharField(max_length=100,blank=True, null=True)
    square_m_build = models.CharField(max_length=100,blank=True, null=True)
    e_construction_m = models.CharField(max_length=100,blank=True, null=True)
    municipal_n = models.PositiveIntegerField(blank=True, null=True)
    n_building_permit = models.PositiveIntegerField(blank=True, null=True)
    #contables internos
    value_land = models.CharField(max_length=100,blank=True, null=True)
    value_construction = models.CharField(max_length=100,blank=True, null=True)
    contract_type = models.OneToOneField(Document, on_delete=models.CASCADE, related_name='TipoContratoArriendo')
    acquiring_name = models.CharField(max_length=100)
    supplier_name = models.CharField(max_length=100)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    duration = models.PositiveIntegerField()

#Post
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    author = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    publish_date = models.DateTimeField(default=timezone.now)
    acquisition = models.OneToOneField(Acquisition, on_delete=models.CASCADE, related_name='PostAcquisition')
    rent = models.OneToOneField(Rent, on_delete=models.CASCADE, related_name='PostRent')

    def getDiference(self):
        now = datetime.now(timezone.utc)
        difference = now - self.publish_date
        return int(difference.total_seconds() / 3600)
