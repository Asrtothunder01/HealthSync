from rest_framework import serializers

from .models import Appointment

from doctor.serializers import DoctorSerializer

from patient.serializers import PatientSerializer

class AppointmentSerializer(serializers.ModelSerializer):

    doctor = DoctorSerializer(read_only = True)

    patient = PatientSerializer(read_only = True)

    class Meta:
        model = Appointment

        fields = ['id','doctor','patient','appointment_date','symptoms']