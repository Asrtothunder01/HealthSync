from rest_framework import serializers

from .models import DietPlan

from user.serializers import FitnessSerializer

class DietSerializer(serializers.ModelSerializer):
    fitness_user = FitnessSerializer(read_only = True)

    class Meta:
        
        model = DietPlan

        fields = ['id','fitness_user','name','calories_per_day']