from rest_framework import serializers
from user.serializers import UserSerializer
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    class Meta:
        model = Doctor

        fields = ['id','user','specialization','phone_number','address']