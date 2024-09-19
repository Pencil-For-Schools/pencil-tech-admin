import pytz
from django.utils.timezone import localtime
from rest_framework import serializers

from admin_app.models import School
from admin_app.utils import format_date_time


class SchedulesSerializer(serializers.Serializer):
    def to_representation(self, instance):
        date, formatted_time = format_date_time(instance.date_time)
        return {
          "id": instance.id,
          "date": date,
          "time": formatted_time,
          "location": {
            "id": instance.pencil_box_location.id,
            "availability": instance.shopper_qty,
            "loc": instance.pencil_box_location.name
          }
        }

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id', 'name')
        model=School
