from django.urls import path
from Auth_users import views

urlpatterns = [
    path('login/', views.login, name="_login"),
    path('logout/', views.auth_logout, name="auth_logout"),
]