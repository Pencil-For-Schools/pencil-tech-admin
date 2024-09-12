from django.db import models
from .school import School
from .county import County


class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    school = models.ForeignKey(
        School, on_delete=models.PROTECT, related_name='teachers')
    email = models.EmailField()
    phone = models.CharField(max_length=55)
    pencil_id = models.IntegerField()
    county = models.ForeignKey(County, on_delete=models.PROTECT)
    archived = models.BooleanField(default=False)
