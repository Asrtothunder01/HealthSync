from django.db import models
from user.models import FitnessUser
# Create your models here.

class DietPlan(models.Model):
    fitness_user = models.ForeignKey(FitnessUser,on_delete = models.CASCADE,null= True )

    name = models.CharField(max_length = 100)

    calories_per_day = models.IntegerField()