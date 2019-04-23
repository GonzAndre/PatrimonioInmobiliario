from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name="index"),
    path('list_acquisitions', views.list_acquisition, name="list_acquisitions"),
    path('add_property/',views.Add_acquisition, name = "add_property"),
    path('login/', views.login, name="_login"),
    path('logout/', views.auth_logout, name="auth_logout"),

    path('editar_acquisition/<int:acq_id>', views.Edit_acquisition, name="edit_acquisition"),
    path('delete_acquisition/<int:id>', views.Delete_acquisition, name="delete_acquisition"),

    path('editar_rent/<int:rent_id>', views.Edit_rent, name="edit_rent"),
    path('delete_rent/<int:id>', views.Delete_rent, name="delete_rent"),
]
