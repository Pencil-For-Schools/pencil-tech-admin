from rest_framework import generics
from admin_app.serializers.scheduling_serializers import SchoolSerializer
from admin_app.models import School

class SchoolList(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
