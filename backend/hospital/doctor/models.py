import uuid

from django.db import models

from django.contrib.auth.models import User

class BaseModel (models.Model):
    id = models.UUIDField(unique = True, editable = True, primary_key = True, default = uuid.uuid4)
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        abstract = True
        

class Doctor(BaseModel):
    
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    
    specialization = models.CharField(max_length = 50)
    
    address = models.CharField()
    
    def __str__(self):
        return f"Dr.{self.user.first_name}{self.last_name}-{self.specialization}"