from django.db import models
from .school import School
from .county import County


class Teacher(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    school = models.ForeignKey(
        School, on_delete=models.PROTECT, related_name='teachers')
    email = models.EmailField()
    phone = models.CharField(max_length=55, null=True, blank=True)
    pencil_id = models.IntegerField(null=True, blank=True)
    county = models.ForeignKey(County, on_delete=models.PROTECT, null=True, blank=True)
    archived = models.BooleanField(default=False)
