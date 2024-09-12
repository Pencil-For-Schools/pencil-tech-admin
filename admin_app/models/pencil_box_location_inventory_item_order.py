from django.db import models
from .order import Order
from .pencil_box_location_inventory_item import PencilBoxLocationInventoryItem

class PencilBoxLocationInventoryItemOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    pencil_box_location_inventory_item = models.ForeignKey(PencilBoxLocationInventoryItem, on_delete=models.PROTECT)
    qty = models.PositiveIntegerField()
    value = models.FloatField()
    