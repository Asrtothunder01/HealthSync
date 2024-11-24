from rest_framework import serializers

from .models import FitnessUser

class FitnessSerializer(serializers.ModelSerializer):

    class Meta:

        model = FitnessUser

        fields = ['id','height','weight','goal']
