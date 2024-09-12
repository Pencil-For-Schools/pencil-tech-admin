# I need the teacher and pencil_box_location_inventory_item
from admin_app.models import PencilBoxLocationInventoryItemOrder, PencilBoxLocationInventoryItem
from rest_framework.response import Response
from django.http import HttpResponseBadRequest
from admin_app.serializers.inventory_app import PencilBoxLocationInventoryItemSerializer
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def inventory_items(request, location_id):
    '''Get all the inventory items by location'''
    try:

        pencil_box_location_inventory_items = PencilBoxLocationInventoryItem.objects.filter(pencil_box_location_id=location_id).order_by('-bin_number')

        if not pencil_box_location_inventory_items.exists():
            return Response({"detail": "No items found at this location."}, status=status.HTTP_404_NOT_FOUND)

        in_stock_items = pencil_box_location_inventory_items.filter(in_stock__gt=0)

        serializer = PencilBoxLocationInventoryItemSerializer(in_stock_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except PencilBoxLocationInventoryItem.DoesNotExist:
        return HttpResponseBadRequest("I could not find any items at the specified location.")

    except Exception as e:
        return HttpResponseBadRequest(f"An error occurred: {str(e)}")
