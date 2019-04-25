from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name="index"),
    path('list_acquisition', views.list_acquisition, name="list_acquisition"),
    path('list_rent', views.list_rent, name="list_rent"),
    path('add_acquisition/',views.Add_acquisition, name = "add_acquisition"),
    path('editar_acquisition/<int:acq_id>', views.Edit_acquisition, name="edit_acquisition"),
    path('delete_acquisition/<int:id>', views.Delete_acquisition, name="delete_acquisition"),
    path('editar_rent/<int:rent_id>', views.Edit_rent, name="edit_rent"),
    path('delete_rent/<int:id>', views.Delete_rent, name="delete_rent"),
    path('view_acquisition/<int:cli_id>', views.view_acquisition, name="view_acquisition"),
    path('view_rent/<int:rent_id>', views.view_rent, name="view_rent"),
]
