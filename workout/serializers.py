from rest_framework import serializers

from .models import WorkoutExercise,WorkoutRoutine,WorkoutSession



class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutRoutine

        fields = ['id','name','description','created_by']


class ExerciseSerializer(serializers.ModelSerializer):

    workout_routine = RoutineSerializer(read_only = True)
    
    class Meta:
        model = WorkoutExercise

        fields = ['id','workout_routine','exercise','sets','reps']

class SessionSerializer(serializers.ModelSerializer):
    workout_routine = RoutineSerializer(read_only = True)

    class Meta:
        model = WorkoutSession

        fields = ['id','fitness_user','workout_routine','date','duration']

