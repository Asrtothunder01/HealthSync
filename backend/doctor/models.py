from django.db import models
from user.models import CustomUser
# Create your models here.

class Doctor(models.Model):
    user = models.OneToOneField(CustomUser,on_delete = models.CASCADE,null=True)
    specialization = models.CharField(max_length = 100)
    phone_number= models.CharField(max_length= 15)
    address = models.TextField()

    def __str__(self):
        return f'Dr {self.user.firstname} {self.user.last_name}-{self.specialization}'
