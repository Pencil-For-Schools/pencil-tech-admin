from django.db import models

from .school import School
from .teacher import Teacher


class Order(models.Model):
    teacher = models.ForeignKey(
        Teacher, on_delete=models.PROTECT, related_name='orders')
    school = models.ForeignKey(
        School, on_delete=models.PROTECT, related_name='teacher_orders')
    pickup = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True)
    fullfilled_at = models.DateField(blank=True, null=True)
    approved = models.BooleanField(default=False)
