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
    #path('password_reset', views.password_reset, {'template_name':'password_reset_form.html', 'email_template_name': 'password_reset_email.html'}, name='password_reset'),
    #path('password_reset_done', views.password_reset_done, {'template_name':'password_reset_done.html'}, name='password_reset_done'),
    #path('(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.password_reset_confirm, {'template_name':'password_reset_confirm.html'}, name='password_reset_confirm'),
    #path('password_reset_complete', views.password_reset_complete, {'template_name':'password_reset_complete.html'} , name='password_reset_complete'),
    path('forgotPassword/',views.Forgot_password, name='Login_forgot_password'),
    path('emailPassword/',views.Email_password, name='Login_email_password'),
    path('validate/',views.Validate, name='Login_validate'),
    path('validatePassword/',views.Validate_password, name='Login_validate_password'),

]
