from rest_framework import generics
from admin_app.serializers.scheduling_serializers import AvailableSchedulesSerializer
from admin_app.models import ScheduleItem

class ScheduleList(generics.ListAPIView):
    queryset = ScheduleItem.objects.all()
    serializer_class = AvailableSchedulesSerializer

    def get_queryset(self):
        queryset = ScheduleItem.objects.all()
        available = self.request.query_params.get('available')
        if available:
            queryset = ScheduleItem.available_schedule_items.all()

        return queryset
