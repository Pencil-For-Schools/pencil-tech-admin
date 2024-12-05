from django.db import models
from admin_app.utils import format_date_time
from .teacher import Teacher
from .schedule_item import ScheduleItem
from .order import Order


class TeacherScheduleItem(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    schedule_item = models.ForeignKey(ScheduleItem, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        date, _ = format_date_time(self.schedule_item.date_time)
        return f'{self.teacher.first_name} {self.teacher.last_name}, {date}'
