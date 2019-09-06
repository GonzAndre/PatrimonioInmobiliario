# -*- coding: utf-8 -*-
from django.db import models
from propiedades2.defines import *
from django.contrib.auth.models import User
from django.utils import timezone
from simple_history.models import HistoricalRecords



# Create your models here.
class Region(models.Model):
    acronym = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "Acronimo: %s, nombre: %s" % (self.acronym, self.name)

class Property(models.Model):
    acronym = models.CharField(max_length = 3, blank = True, null = True)
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "Acronimo: %s, nombre: %s" % (self.acronym, self.name)


class Location(models.Model):
    street = models.CharField(max_length=200)
    number = models.PositiveIntegerField()
    commune = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    lot_number = models.PositiveIntegerField(blank=True, null=True)
    plot = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "calle: %s %s" % (self.street, self.number)


# Documentos de arquitectura

class DocumentEx(models.Model):
    archive = models.FileField(upload_to='Documentos/', blank=True)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=5, choices=ATTRIBUTES_CHOICE)

    def __str__(self):
        return "Documento: %s, Fecha de subida: %s" % (self.archive, self.publish_date)


class DocumentCip(models.Model):
    archive = models.FileField(upload_to='Documentos/', blank=True)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=5, choices=ATTRIBUTES_CHOICE)

    def __str__(self):
        return "Documento: %s, Fecha de subida: %s" % (self.archive, self.publish_date)


class DocumentCn(models.Model):
    archive = models.FileField(upload_to='Documentos/', blank=True)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=5, choices=ATTRIBUTES_CHOICE)

    def __str__(self):
        return "Documento: %s, Fecha de subida: %s" % (self.archive, self.publish_date)


class DocumentBlue(models.Model):
    archive = models.FileField(upload_to='Documentos/', blank=True)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=5, choices=ATTRIBUTES_CHOICE)

    def __str__(self):
        return "Documento: %s, Fecha de subida: %s" % (self.archive, self.publish_date)


class DocumentBuildP(models.Model):
    archive = models.FileField(upload_to='Documentos/', blank=True)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=5, choices=ATTRIBUTES_CHOICE)

    def __str__(self):
        return "Documento: %s, Fecha de subida: %s" % (self.archive, self.publish_date)


class DocumentMR(models.Model):
    archive = models.FileField(upload_to='Documentos/', blank=True)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=5, choices=ATTRIBUTES_CHOICE)

    def __str__(self):
        return "Documento: %s, Fecha de subida: %s" % (self.archive, self.publish_date)


# Documentos Internos

class DocumentTypeC(models.Model):
    archive = models.FileField(upload_to='Documentos/', blank=True)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=5, choices=ATTRIBUTES_CHOICE, default='TC')

    def __str__(self):
        return "Documento: %s, Fecha de subida: %s" % (self.archive, self.publish_date)


class DocumentOther(models.Model):
    archive = models.FileField(upload_to='Documentos/', blank=True)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=5, choices=ATTRIBUTES_CHOICE)

    def __str__(self):
        return "Documento: %s, Fecha de subida: %s" % (self.archive, self.publish_date)


# Documentos Notariales

class DocumentWR(models.Model):
    archive = models.FileField(upload_to='Documentos/', blank=True)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=5, choices=ATTRIBUTES_CHOICE)

    def __str__(self):
        return "Documento: %s, Fecha de subida: %s" % (self.archive, self.publish_date)


class DocumentDC(models.Model):
    archive = models.FileField(upload_to='Documentos/', blank=True)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=5, choices=ATTRIBUTES_CHOICE)

    def __str__(self):
        return "Documento: %s, Fecha de subida: %s" % (self.archive, self.publish_date)


class DocumentPH(models.Model):
    archive = models.FileField(upload_to='Documentos/', blank=True)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=5, choices=ATTRIBUTES_CHOICE)

    def __str__(self):
        return "Documento: %s, Fecha de subida: %s" % (self.archive, self.publish_date)


class DocumentEs(models.Model):
    archive = models.FileField(upload_to='Documentos/', blank=True)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=5, choices=ATTRIBUTES_CHOICE)

    def __str__(self):
        return "Documento: %s, Fecha de subida: %s" % (self.archive, self.publish_date)


# Documentos de SII

class DocumentAc(models.Model):
    archive = models.FileField(upload_to='Documentos/', blank=True)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=5, choices=ATTRIBUTES_CHOICE)

    def __str__(self):
        return "Documento: %s, Fecha de subida: %s" % (self.archive, self.publish_date)


class DocumentDB(models.Model):
    archive = models.FileField(upload_to='Documentos/', blank=True)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=5, choices=ATTRIBUTES_CHOICE)

    def __str__(self):
        return "Documento: %s, Fecha de subida: %s" % (self.archive, self.publish_date)


class ArchitectureRecordAcq(models.Model):
    # Antecedentes de arquitectura
    ground_surface = models.CharField(max_length=100, blank=True, null=True)
    square_m_build = models.CharField(max_length=100, blank=True, null=True)
    e_construction_m = models.CharField(max_length=100, blank=True, null=True)
    municipal_n = models.PositiveIntegerField(blank=True, null=True)
    n_building_permit = models.PositiveIntegerField(blank=True, null=True)
    # Documentos de arquitectura
    expropriation_mun = models.ForeignKey(DocumentEx, on_delete=models.CASCADE, blank=True, null=True,
                                          related_name='ExMunicipalidad')
    cip = models.ForeignKey(DocumentCip, on_delete=models.CASCADE, blank=True, null=True,
                            related_name='Cip')
    certified_number = models.ForeignKey(DocumentCn, on_delete=models.CASCADE, blank=True, null=True,
                                         related_name='NumCertificado')
    blueprints = models.ForeignKey(DocumentBlue, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='Planos')
    building_permit = models.ForeignKey(DocumentBuildP, on_delete=models.CASCADE, blank=True, null=True,
                                        related_name='PerEdificacion')
    municipal_reception = models.ForeignKey(DocumentMR, on_delete=models.CASCADE, blank=True, null=True,
                                            related_name='RecMunicipal')


class InternalAccountantsAcq(models.Model):
    value_land = models.CharField(max_length=100, blank=True, null=True)
    value_construction = models.CharField(max_length=100, blank=True, null=True)
    acquiring_name = models.CharField(max_length=100, blank=True, null=True)
    supplier_name = models.CharField(max_length=100, blank=True, null=True)
    contract_type = models.ForeignKey(DocumentTypeC, on_delete=models.CASCADE, related_name='TipoContratoAdquisicion')
    others = models.ForeignKey(DocumentOther, on_delete=models.CASCADE, blank=True, null=True, related_name='Otros')


class NotaryAcquisition(models.Model):
    notary = models.CharField(max_length=100, blank=True, null=True)
    writing_year = models.PositiveIntegerField(blank=True, null=True)
    sale_price = models.CharField(max_length=100, blank=True, null=True)
    # antecedentes de dominio
    previous_title = models.CharField(max_length=100, blank=True, null=True)
    current_title = models.CharField(max_length=100, blank=True, null=True)
    writing = models.ForeignKey(DocumentWR, on_delete=models.CASCADE, blank=True, null=True,
                                related_name='Escritura')
    domain_certificate = models.ForeignKey(DocumentDC, on_delete=models.CASCADE, null=True, blank=True,
                                           related_name='CertificadoDominio')
    prohibitions = models.ForeignKey(DocumentPH, on_delete=models.CASCADE, blank=True, null=True,
                                     related_name='Prohibiciones')
    expropriation_serviu = models.ForeignKey(DocumentEs, on_delete=models.CASCADE, blank=True, null=True,
                                             related_name='Serviu')


class SiiRecord(models.Model):
    destiny = models.CharField(max_length=100, blank=True, null=True)
    tax_appraisal = models.PositiveIntegerField(blank=True, null=True)
    owner_name_SII = models.CharField(max_length=100, blank=True, null=True)
    total_debt = models.PositiveIntegerField(blank=True, null=True)
    ex_contributions = models.BooleanField(default=False)
    # SII - TGR
    appraisal_certificate = models.ForeignKey(DocumentAc, on_delete=models.CASCADE, blank=True, null=True,
                                              related_name='CerAvaluo')
    debt_certificate = models.ForeignKey(DocumentDB, on_delete=models.CASCADE, blank=True, null=True,
                                         related_name='CerNoDeuda')


class Acquisition(models.Model):
    name = models.CharField(max_length=200)
    role_number = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='Fotos/', blank=True, null=True)
    property_use = models.ForeignKey(Property, on_delete=models.CASCADE)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    acquisition_date = models.DateTimeField(default=timezone.now)
    writing_data = models.CharField(max_length=5, choices=WRITING_DATA_CHOICE)
    number_AASI = models.PositiveIntegerField()
    arquitecture = models.OneToOneField(ArchitectureRecordAcq, on_delete=models.CASCADE, blank=True, null=True,
                                        related_name='arquitecture_acq')
    internal = models.OneToOneField(InternalAccountantsAcq, on_delete=models.CASCADE, blank=True, null=True,
                                    related_name='internal_acq')
    notary = models.OneToOneField(NotaryAcquisition, on_delete=models.CASCADE, blank=True, null=True,
                                  related_name='notary_acq')
    SII = models.OneToOneField(SiiRecord, on_delete=models.CASCADE, blank=True, null=True, related_name='SII_acq')
    status = models.BooleanField(default=True)
    historyl = HistoricalRecords()
    def __str__(self):
        return "nombre: %s, rol: %s, uso: %s" % (self.name, self.role_number, self.property_use)


class Rent(models.Model):
    name = models.CharField(max_length=200)
    role_number = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='Fotos/', blank=True, null=True)
    property_use = models.ForeignKey(Property, on_delete=models.CASCADE)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    # antecedentes de arquitectura
    ground_surface = models.CharField(max_length=100, blank=True, null=True)
    square_m_build = models.CharField(max_length=100, blank=True, null=True)
    e_construction_m = models.CharField(max_length=100, blank=True, null=True)
    municipal_n = models.PositiveIntegerField(blank=True, null=True)
    n_building_permit = models.PositiveIntegerField(blank=True, null=True)
    # contables internos
    value_land = models.CharField(max_length=100, blank=True, null=True)
    value_construction = models.CharField(max_length=100, blank=True, null=True)
    contract_type = models.OneToOneField(DocumentTypeC, blank=True, null=True, on_delete=models.CASCADE,
                                         related_name='TipoContratoArriendo')
    acquiring_name = models.CharField(max_length=100)
    supplier_name = models.CharField(max_length=100)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    duration = models.PositiveIntegerField()
    historyl = HistoricalRecords()
    status = models.BooleanField(default=True)
    def __str__(self):
        return "Nombre: %s" % (self.name)

class Staff(models.Model):
    username_staff = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    type_user = models.CharField(max_length=3, choices=POSITION_CHOICE)
    status = models.BooleanField(default=True)
    email = models.EmailField()

    def __str__(self):
        return "username: %s Tipo de usuario: %s" % (self.username_staff, self.type_user)

# Post
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    author = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    publish_date = models.DateTimeField(default=timezone.now)
    acquisition = models.OneToOneField(Acquisition, on_delete=models.CASCADE, related_name='PostAcquisition')
    rent = models.OneToOneField(Rent, on_delete=models.CASCADE, related_name='PostRent')

    def getDiference(self):
        now = datetime.now(timezone.utc)
        difference = now - self.publish_date
        return int(difference.total_seconds() / 3600)
