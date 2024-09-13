from rest_framework import generics
from admin_app.serializers.scheduling_serializers import SchedulesSerializer
from admin_app.models import ScheduleItem

class ScheduleRetrieve(generics.RetrieveAPIView):
    queryset = ScheduleItem.objects.all()
    serializer_class = SchedulesSerializer
