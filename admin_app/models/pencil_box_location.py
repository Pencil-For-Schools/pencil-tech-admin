from django.db import models


class PencilBoxLocation(models.Model):
    name = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name
