from django.db import models
from .teacher import Teacher
from .schedule_item import ScheduleItem
from .order import Order


class TeacherScheduleItem(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    schedule_item = models.ForeignKey(ScheduleItem, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
