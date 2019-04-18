from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name="index"),
    path('list_property', views.list_property, name="list_property"),
    path('view/<int:cli_id>', views.view_acquisition, name="view_acquisition"),
    # path('login/', views.login, name="_login"),
    # path('logout/', views.auth_logout, name="auth_logout"),
]
