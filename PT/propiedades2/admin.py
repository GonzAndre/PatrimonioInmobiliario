from django.contrib import admin
from propiedades2.models import Acquisition, DocumentEx, DocumentCip, DocumentCn, DocumentBlue, DocumentBuildP, \
    DocumentMR, DocumentTypeC, DocumentOther, DocumentWR, DocumentDC, DocumentPH, DocumentDB, DocumentAc, DocumentEs, \
    Location,ArchitectureRecordAcq, InternalAccountantsAcq, NotaryAcquisition, SiiRecord, Rent, Post, Staff, Region, Property, Change_property, \
    Comment, Stats, District, Report, Notification
from reversion.admin import VersionAdmin

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
admin.site.register(District)
admin.site.register(Change_property)
admin.site.unregister(Change_property)
admin.site.unregister(Location)
admin.site.unregister(Acquisition)
admin.site.unregister(ArchitectureRecordAcq)
admin.site.unregister(InternalAccountantsAcq)
admin.site.unregister(NotaryAcquisition)
admin.site.unregister(SiiRecord)
admin.site.unregister(DocumentEx)
admin.site.unregister(DocumentCip)
admin.site.unregister(DocumentCn)
admin.site.unregister(DocumentBlue)
admin.site.unregister(DocumentBuildP)
admin.site.unregister(DocumentMR)
admin.site.unregister(DocumentTypeC)
admin.site.unregister(DocumentOther)
admin.site.unregister(DocumentWR)
admin.site.unregister(DocumentDC)
admin.site.unregister(DocumentPH)
admin.site.unregister(DocumentDB)
admin.site.unregister(DocumentAc)
admin.site.unregister(DocumentEs)
admin.site.unregister(Post)
admin.site.unregister(Rent)
admin.site.unregister(Staff)
admin.site.unregister(Region)
admin.site.register(Property)
admin.site.register(Report)
admin.site.register(Notification)
admin.site.unregister(Property)
admin.site.unregister(District)
@admin.register(Property)
class propertyAdmin(VersionAdmin):
    pass
@admin.register(Location)
class locationAdmin(VersionAdmin):
    pass
@admin.register(Acquisition)
class acquisitionAdmin(VersionAdmin):
    pass
@admin.register(ArchitectureRecordAcq)
class architectureRecordAcqAdmin(VersionAdmin):
    pass
@admin.register(InternalAccountantsAcq)
class internalAccountantsAcqAdmin(VersionAdmin):
    pass
@admin.register(NotaryAcquisition)
class notaryAcquisitionAdmin(VersionAdmin):
    pass
@admin.register(SiiRecord)
class siiRecordAdmin(VersionAdmin):
    pass
@admin.register(DocumentEx)
class documentExAdmin(VersionAdmin):
    pass
@admin.register(DocumentCip)
class documentCipAdmin(VersionAdmin):
    pass
@admin.register(DocumentCn)
class documentCnAdmin(VersionAdmin):
    pass
@admin.register(DocumentBlue)
class documentBlueAdmin(VersionAdmin):
    pass
@admin.register(DocumentBuildP)
class documentBuildPAdmin(VersionAdmin):
    pass
@admin.register(DocumentMR)
class documentMRAdmin(VersionAdmin):
    pass
@admin.register(DocumentTypeC)
class documentTypeCAdmin(VersionAdmin):
    pass
@admin.register(DocumentOther)
class documentOtherAdmin(VersionAdmin):
    pass
@admin.register(DocumentWR)
class documentWRAdmin(VersionAdmin):
    pass
@admin.register(DocumentDC)
class documentDCAdmin(VersionAdmin):
    pass
@admin.register(DocumentPH)
class documentPHAdmin(VersionAdmin):
    pass
@admin.register(DocumentDB)
class documentDBAdmin(VersionAdmin):
    pass
@admin.register(DocumentAc)
class documentAcAdmin(VersionAdmin):
    pass
@admin.register(DocumentEs)
class documentEsAdmin(VersionAdmin):
    pass
@admin.register(Post)
class postAdmin(VersionAdmin):
    pass
@admin.register(Rent)
class rentAdmin(VersionAdmin):
    pass
@admin.register(Staff)
class staffAdmin(VersionAdmin):
    pass
@admin.register(Region)
class regionAdmin(VersionAdmin):
    pass
@admin.register(Change_property)
class change_propertyAdmin(VersionAdmin):
    pass
@admin.register(Comment)
class commentAdmin(VersionAdmin):
    pass
@admin.register(Stats)
class statsAdmin(VersionAdmin):
    pass
@admin.register(District)
class districtAdmin(VersionAdmin):
    pass
