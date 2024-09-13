from rest_framework import generics
from admin_app.serializers.scheduling_serializers import SchedulesSerializer
from admin_app.models import ScheduleItem

class ScheduleList(generics.ListAPIView):
    queryset = ScheduleItem.available_schedule_items.all()
    serializer_class = SchedulesSerializer

    def get_queryset(self):
        queryset = ScheduleItem.available_schedule_items.all()
        month = self.request.query_params.get('month')
        if month:
            queryset = queryset.filter(date_time__month=month)

        return queryset
