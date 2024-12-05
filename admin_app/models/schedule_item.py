from django.db import models
from django.utils import timezone
from admin_app.utils import format_date_time
from .pencil_box_location import PencilBoxLocation

class AvailableSchedulesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(date_time__gte=timezone.now())

class ScheduleItem(models.Model):
    shopper_qty = models.IntegerField()
    date_time = models.DateTimeField()
    pencil_box_location = models.ForeignKey(
        PencilBoxLocation, on_delete=models.PROTECT, related_name='schedule_items')   # noqa: E501

    objects = models.Manager()
    available_schedule_items = AvailableSchedulesManager()

    def __str__(self):
        date, _ = format_date_time(self.date_time)
        return f'{self.pencil_box_location.name}, {date}'
