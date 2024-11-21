from rest_framework import serializers

from .models import Meal

from diet.serializers import DietSerializer

class MealSerializer(serializers.ModelSerializer):
    
    diet_plan = DietSerializer(read_only = True)

    class Meta:
        model = Meal

        fields = ['id','diet_plan','meal_name','calories','protein','carbs','fats']