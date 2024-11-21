from django.db import models
from doctor.models import Doctor
from patient.models import Patient

# Create your models here.

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete= models.CASCADE,null = True)

    Patient = models.ForeignKey(Patient,on_delete= models.CASCADE, null = True)

    appointment_date = models.DateField()

    symptoms = models.TextField()

    