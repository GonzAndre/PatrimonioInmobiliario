from django.db import models
from Auth_users.defines import *
from django.contrib.auth.models import User as Username
# Create your models here.
class UserProfile(models.Model):
    username = models.OneToOneField(Username,null=True, default=None, on_delete=models.CASCADE)
    password = models.CharField(max_length=50)
