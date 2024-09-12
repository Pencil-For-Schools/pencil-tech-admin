from rest_framework import serializers
from django.utils.timezone import localtime
import pytz

class AvailableSchedulesSerializer(serializers.Serializer):
    def to_representation(self, instance):
        date = instance.date_time.strftime('%B %d, %Y')
        time = localtime(instance.date_time, pytz.timezone('America/Chicago'))
        formatted_time = time.strftime('%I:%M %p CST')
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
