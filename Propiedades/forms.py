from django.forms import ModelForm
from Property.models import *
from Auth_users.models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DocumentForm(ModelForm):

    class meta:
        model = Document
        fields = ['archive','publish_date','comment',]

class LocationForm(ModelForm):

    class meta:
        model = Location
        fields = ['street','number','commune','city','region','lot_number','plot',]

class PropertyForm(ModelForm):

    class meta:
        model = Property
        fields = ['name','role_number','image','property_use','location','ground_surface','square_m_build','e_construction_m','municipal_n','n_building_permit','value_land','value_construction',]

class PostForm(ModelForm):

    class meta:
        model = Post
        fields = ['title','description','author','publish_date','property',]


class AcquisitionForm(ModelForm):

    class meta:
        model = Acquisition
        fields = ['number_AASI','acquisition_date','contract_type','acquiring_name','supplier_name','start_date','notary','writing_year','sale_price','previous_title','current_title',
                  'destiny','tax_appraisal','owner_name_SII','total_debt','ex_contributions','writing','domain_certificate','prohibitions','expropriation_serviu','others','expropriation_mun',
                  'cip','certified_number','blueprints','building_permit','municipal_reception','appraisal_certificate','debt_certificate',]

class RentForm(ModelForm):

    class meta:
        model = Rent
        fields = ['contract_type','acquiring_name','supplier_name','start_date','end_date','duration',]

class UserProfileFrom(ModelForm):

    class meta:
        model = UserProfile
        fields = ['username','password',]
