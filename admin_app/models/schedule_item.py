from django.db import models
from .pencil_box_location import PencilBoxLocation

class ScheduleItem(models.Model):
    shopper_qty = models.IntegerField()
    date_time = models.DateTimeField()
    pencil_box_location = models.ForeignKey(PencilBoxLocation, on_delete=models.SET_NULL, null=True, related_name='schedule_items')
