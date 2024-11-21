from django.db import models
from diet.models import DietPlan
# Create your models here.

class Meal(models.Model):
    diet_plan = models.ForeignKey(DietPlan,on_delete = models.CASCADE,null= True )

    meal_name = models.CharField(max_length = 100)

    calories = models.IntegerField()

    protein = models.DecimalField(max_digits = 5,decimal_places = 2)

    carbs = models.DecimalField(max_digits=5,decimal_places=2)

    fats = models.DecimalField(max_digits =5,decimal_places=2)
    