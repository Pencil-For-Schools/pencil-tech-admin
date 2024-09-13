from django.db import models


class PencilBoxLocation(models.Model):
    name = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=255, blank=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name
