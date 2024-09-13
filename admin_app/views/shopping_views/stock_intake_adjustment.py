from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from admin_app.models import PencilBoxLocationInventoryItem, PencilBoxLocation, InventoryItem, InventoryIntake, IntakeType
from django.contrib.auth.models import User

class InventoryIntakeOrAdjustment(APIView):

    def post(self, request):

        item = InventoryItem.objects.get(pk=request.data.get("item_id"))
        location =  PencilBoxLocation.objects.get(pk=request.data.get("location_id"))
        intake_type = IntakeType.objects.get(pk=request.data.get('intake_type_id'))

        location_item = PencilBoxLocationInventoryItem.objects.filter(inventory_item=item, pencil_box_location=location)

        location_item.in_stock += request.data.get('qty')
        location_item.save()

        InventoryIntake.create(
            inventory_item = item,
            updated_by = User.objects.get(username=request.user),
            donated_by = request.data.get('donated_by', None),
            qty_donated = request.data.get('qty'),
            pencil_box_location = location,
            notes = request.data.get('notes'),
            updated_at = datetime.now(),
            intake_type = intake_type
        )

        return Response({"message": "INTAKE_SUCCESS"}, status=status.HTTP_201_CREATED)
