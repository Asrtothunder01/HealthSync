from rest_framework import serializers

from .models import MedicalRecord
from doctor.serializers import DoctorSerializer

from patient.serializers import PatientSerializer

class MedicalSerializer(serializers.ModelSerializer):

    patient = PatientSerializer(read_only = True)

    doctor = DoctorSerializer(read_only = True)



    class Meta:
        model = MedicalRecord

        fields = ['id','patient','doctor','diagnosis','record_date','treatment']