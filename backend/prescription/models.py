from django.db import models

from records.models import MedicalRecord

# Create your models here.

class Prescription(models.Model):
    medical_record= models.ForeignKey(MedicalRecord,on_delete= models.CASCADE,null = True)

    medical_name = models.CharField(max_length= 100)

    dosage = models.CharField(max_length = 50)

    duration = models.CharField(max_length=50)

    notes = models.TextField(blank= True)

    