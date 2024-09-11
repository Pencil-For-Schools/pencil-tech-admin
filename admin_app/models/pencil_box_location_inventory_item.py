from django.db import models

from .inventory_item import InventoryItem
from .pencil_box_location import PencilBoxLocation


class PencilBoxLocationInventoryItem(models.Model):
    inventory_item = models.ForeignKey(
        InventoryItem, on_delete=models.PROTECT, related_name='pencil_box_locations')
    pencil_box_location = models.ForeignKey(
        PencilBoxLocation, on_delete=models.PROTECT, related_name='inventory_items')
    bin_number = models.IntegerField()
    low_stock = models.IntegerField()
    max_amt = models.IntegerField()
    sold = models.IntegerField()
    in_stock = models.IntegerField()
    last_audited = models.DateTimeField()
    archived = models.BooleanField(default=False)
