from rest_framework import serializers
from user.serializers import UserSerializer
from .models import  Patient

class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    class Meta:
        model = Patient

        fields = ['id','user','dob','phone_number','address']
