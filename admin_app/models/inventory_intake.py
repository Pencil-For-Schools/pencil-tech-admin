from django.db import models

from .intake_type import IntakeType
from .inventory_item import InventoryItem
from .pencil_box_location import PencilBoxLocation
from django.contrib.auth.models import User


class InventoryIntake(models.Model):
    inventory_item = models.ForeignKey(
        InventoryItem, on_delete=models.PROTECT, related_name='intakes')
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='update_users')
    donated_by = models.CharField(max_length=255)
    qty_donated = models.PositiveIntegerField()
    pencil_box_location = models.ForeignKey(
        PencilBoxLocation, on_delete=models.PROTECT)
    notes = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    intake_type = models.ForeignKey(IntakeType, on_delete=models.PROTECT)
