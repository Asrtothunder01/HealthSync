from rest_framework import serializers

from doctor.models import Doctor

from patient.models import Patient

class RecordSerializer(serializers.ModelSerializer):
  
    doctor = DoctorSerializer(many = True)
    
    patient = PatientSerializer(many = True)
    
    class Meta:
        model = Record
        
        fields = ['id','doctor','patient','symptoms','appointment_date','created_at','updated_at']
        
        read_only_fields = ['id','created_at','updated_at']
        
        