from django.contrib import admin
from .models import Document, Location, Post, Property, Acquisition, Rent
# Register your models here.

admin.site.register(Document)
admin.site.register(Location)
admin.site.register(Post)
admin.site.register(Property)
admin.site.register(Acquisition)
admin.site.register(Rent)