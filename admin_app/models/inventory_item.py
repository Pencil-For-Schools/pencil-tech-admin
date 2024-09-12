from django.db import models


class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    value = models.FloatField()
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name
