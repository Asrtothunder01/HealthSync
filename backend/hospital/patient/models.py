import uuid

from django.db import models

from django.contrib.auth.models import User

class BaseModel (models.Model):
    id = models.UUIDField(unique = True, editable = True, primary_key = True, default = uuid.uuid4)
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        abstract = True
        

class Patient(BaseModel):
    
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    
    dob = models.PositiveIntegerField(max_length = 15)
    
    contact = models.CharField(max_length = 15)
    
    address = models.TextField()
    
    def __str__(self):
        return f"{self.user.first_name}{self.last_name}"