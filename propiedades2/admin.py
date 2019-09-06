from django.contrib import admin
from propiedades2.models import Acquisition, DocumentEx, DocumentCip, DocumentCn, DocumentBlue, DocumentBuildP, \
    DocumentMR, DocumentTypeC, DocumentOther, DocumentWR, DocumentDC, DocumentPH, DocumentDB, DocumentAc, DocumentEs, \
    Location,ArchitectureRecordAcq, InternalAccountantsAcq, NotaryAcquisition, SiiRecord, Rent, Post, Staff, Region, Property
# Register your models here.

admin.site.register(Location)
admin.site.register(Acquisition)
admin.site.register(ArchitectureRecordAcq)
admin.site.register(InternalAccountantsAcq)
admin.site.register(NotaryAcquisition)
admin.site.register(SiiRecord)
admin.site.register(DocumentEx)
admin.site.register(DocumentCip)
admin.site.register(DocumentCn)
admin.site.register(DocumentBlue)
admin.site.register(DocumentBuildP)
admin.site.register(DocumentMR)
admin.site.register(DocumentTypeC)
admin.site.register(DocumentOther)
admin.site.register(DocumentWR)
admin.site.register(DocumentDC)
admin.site.register(DocumentPH)
admin.site.register(DocumentDB)
admin.site.register(DocumentAc)
admin.site.register(DocumentEs)
admin.site.register(Post)
admin.site.register(Rent)
admin.site.register(Staff)
admin.site.register(Region)
admin.site.register(Property)
