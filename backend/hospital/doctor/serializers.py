from rest_framework import serializers

from django.contrib.auth.models import User

class DoctorSerializer (serializers.ModelSerializer):
    
    user = UserSerializer (read_only = True)
    
    class Meta:
        model = Doctor
        
        fields = ['id','user','specialization','contact','address','created_at','updated_at']
        
        read_only_fields = ['id','created_at','updated_at']
        
        