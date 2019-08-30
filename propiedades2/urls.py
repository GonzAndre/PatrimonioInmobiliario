from django.urls import path
from propiedades2 import views


urlpatterns = [
    path('index', views.index, name="index"),
    path('view_archive/<str:document_type>/<str:document_id>', views.view_archive, name="view_archive"),
    path('list_total', views.list_total, name="list_total"),
    path('list_acquisitions', views.list_acquisition, name="list_acquisition"),
    path('add_acquisition',views.Add_acquisition, name = "add_acquisition"),
    path('editar_acquisition/<int:acq_id>', views.Edit_acquisition, name="edit_acquisition"),
    path('delete_acquisition/<int:id>', views.Delete_acquisition, name="delete_acquisition"),
    path('view/<int:cli_id>', views.view_acquisition, name="view_acquisition"),
    path('list_rent', views.list_rent, name="list_rent"),
    path('add_rent',views.Add_rent, name = "add_rent"),
    path('editar_rent/<int:rent_id>', views.Edit_rent, name="edit_rent"),
    path('delete_rent/<int:id>', views.Delete_rent, name="delete_rent"),
    path('view_rent/<int:rent_id>', views.view_rent, name="view_rent"),
    path('search', views.search, name="search"),
    path('createstaff/', views.createstaff, name='createstaff'),
    path('edit_staff/<int:staff_id>', views.edit_staff, name='edit_staff'),
    path('list_staff', views.list_staff, name="list_staff"),
    path('edit_password/<int:staff_id>', views.edit_password, name="edit_password"),
    path('forgotPassword/',views.Forgot_password, name='Login_forgot_password'),
    path('emailPassword/',views.Email_password, name='Login_email_password'),
    path('validate/',views.Validate, name='Login_validate'),
    path('validatePassword/',views.Validate_password, name='Login_validate_password'),
    path('add_region/', views.add_region, name = 'add_region'),
    path('edit_region/<int:region_id>', views.edit_region, name = 'edit_region'),
    path('list_region', views.list_region, name='list_region'),
    path('delete_region/<int:region_id>', views.delete_region, name='delete_region'),
    path('add_property/', views.add_property, name = 'add_property'),
    path('edit_property/<int:property_id>', views.edit_property, name = 'edit_property'),
    path('list_property', views.list_property, name='list_property'),
    path('delete_property/<int:property_id>', views.delete_property, name='delete_property'),
    path('change_status_rent/<int:id>', views.change_status_rent, name='change_status_rent')
]
