from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    is_lawyer = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

class Lawyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    RUA = models.TextField()

class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)