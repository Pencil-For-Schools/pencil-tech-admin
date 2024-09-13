from django.db import models
from .county import County


class School(models.Model):
    name = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=255, blank=True)
    sales_force_id = models.CharField(max_length=255, null=True, blank=True)
    county = models.ForeignKey(
        County, on_delete=models.PROTECT, related_name='schools')
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name
