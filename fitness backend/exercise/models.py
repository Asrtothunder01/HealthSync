from django.db import models
# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length = 100)

    muscle_group = models.CharField(max_length= 100)

    instructions = models.TextField()

    

    