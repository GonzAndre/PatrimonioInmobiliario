from django.urls import path
from Propiedades import views


urlpatterns = [
    path('index', views.index, name="index"),
    path('list_acquisitions', views.list_acquisition, name="list_acquisitions"),
    path('add_acquisition',views.Add_acquisition, name = "add_acquisition"),
    path('editar_acquisition/<int:acq_id>', views.Edit_acquisition, name="edit_acquisition"),
    path('delete_acquisition/<int:id>', views.Delete_acquisition, name="delete_acquisition"),
    path('view/<int:cli_id>', views.view_acquisition, name="view_acquisition"),

    path('list_rent', views.list_rent, name="list_rents"),
    path('add_rent',views.Add_rent, name = "add_rent"),
    path('editar_rent/<int:rent_id>', views.Edit_rent, name="edit_rent"),
    path('delete_rent/<int:id>', views.Delete_rent, name="delete_rent"),
    path('view_rent/<int:rent_id>', views.view_rent, name="view_rent"),
]
