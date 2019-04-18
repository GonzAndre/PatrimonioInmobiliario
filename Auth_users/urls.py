from django.urls import path
from Auth_users import views


urlpatterns = [
    path('login/',views.auth_login, name='login'),

]
