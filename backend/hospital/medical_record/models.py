import uuid

from django.db import models

from patient.models import Patient

from doctor.models import Doctor

class BaseModel (models.Model):
    id = models.UUIDField(unique = True, editable = True, primary_key = True, default = uuid.uuid4)
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        abstract = True
        

class Record(BaseModel):
    
    patient = models.ForeignKey(Patient,on_delete = models.CASCADE)
    
    doctor = models.ForeignKey(Doctor,on_delete = models.ForeignKey)
    
    treatment = models.TextField()
    
    diagnosis = models.TextField()
    
    record_date = models.DateTimeField()
    
    def __str__(self):
        return f"Medical Record of {self.patient} by {self.doctor} on {self.record_date}"