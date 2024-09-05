from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    sales_force_id = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.name
