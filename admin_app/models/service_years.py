from django.db import models

class ServiceYears(models.Model):
    years = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
