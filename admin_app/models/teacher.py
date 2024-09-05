from django.db import models
from .school import School

class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True,  related_name='teachers')
    email = models.EmailField()
    phone = models.CharField(max_length=55)
    
