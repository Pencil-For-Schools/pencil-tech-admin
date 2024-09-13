from rest_framework import generics
from admin_app.serializers.shopping_serializers import LocationSerializer
from admin_app.models import PencilBoxLocation

class LocationList(generics.ListAPIView):
    queryset = PencilBoxLocation.objects.all()
    serializer_class = LocationSerializer
