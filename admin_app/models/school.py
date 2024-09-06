from django.db import models
from .county import County

class School(models.Model):
    name = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    sales_force_id = models.CharField(max_length=255, null=True, blank=True)
    county = models.ForeignKey(County, on_delete=models.SET_NULL, null=True, related_name='schools')
    
    def __str__(self):
        return self.name
