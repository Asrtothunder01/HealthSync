from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class FitnessUser(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE,null = True)

    height = models.DecimalField(max_digits= 5,decimal_places=2)

    weight = models.DecimalField(max_digits= 5,decimal_places=2)

    goal = models.CharField(max_length = 100)