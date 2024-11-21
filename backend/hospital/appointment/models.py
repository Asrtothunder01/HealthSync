import uuid

from doctor.models import Doctor

from patient.models import Patient

from django.db import models

class BaseModel (models.Model):
    id = models.UUIDField(unique = True, editable = True, primary_key = True, default = uuid.uuid4)
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        abstract = True
        

class Appointmentt(BaseModel):
    
    doctor = models.ForeignKeyField(Doctor,on_delete = models.CASCADE)
    
    patient = models.ForeignKey(Patient,on_delete = models.CASCADE)
    
    symptoms = models.TextField()
    
    appointment_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"Appointment with{self.Doctor} on {self.appointment_date}"
        