from django.db import models
from user.models import FitnessUser
from exercise.models import Exercise
# Create your models here.

class WorkoutRoutine(models.Model):
    name = models.CharField(max_length = 100)

    description = models.TextField()

    created_by = models.ForeignKey(FitnessUser,on_delete = models.CASCADE,null= True)

class WorkoutExercise(models.Model):
    workout_routine = models.ForeignKey(WorkoutRoutine,on_delete = models.CASCADE,null = True)

    exercise = models.ForeignKey(Exercise,on_delete = models.CASCADE,null=True)

    sets = models.IntegerField()

    reps = models.IntegerField() 

class WorkoutSession(models.Model):
    fitness_user = models.ForeignKey(FitnessUser,on_delete=models.CASCADE,null= True)

    workout_routine = models.ForeignKey(WorkoutRoutine,on_delete=models.CASCADE,null=True)

    date = models.DateField()

    duration = models.DurationField()