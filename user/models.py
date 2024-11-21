from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    firstname = models.CharField(max_length = 25)
    email = models.EmailField(unique=True)
    last_name = models.CharField(max_length= 25)