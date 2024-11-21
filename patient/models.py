from django.db import models
from user.models import CustomUser
# Create your models here.

class Patient(models.Model):
    user = models.OneToOneField(CustomUser,on_delete = models.CASCADE,null = True)

    dob = models.DateField()

    phone_number = models.CharField(max_length= 15)

    address = models.TextField()
    