from django.db import models
from .inventory_item import InventoryItem
from .pencil_box_location import PencilBoxLocation
from .intake_type import IntakeType

class InventoryIntake(models.Model):
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.PROTECT, related_name='intakes')
    updated_by = models.CharField(max_length=255)
    donated_by = models.CharField(max_length=255)
    qty_donated = models.CharField(max_length=255)
    pencil_box_location = models.ForeignKey(PencilBoxLocation, on_delete=models.PROTECT)
    notes = models.TextField()
    updated_at = models.DateTimeField()
    intake_type = models.ForeignKey(IntakeType, on_delete=models.PROTECT)
