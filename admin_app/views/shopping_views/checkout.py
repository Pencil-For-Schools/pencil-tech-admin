from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from admin_app.models import PencilBoxLocationInventoryItemOrder, Order, PencilBoxLocationInventoryItem
from integrations.courier.resources.courier_messages.courier_message import CourierMessage

class TeacherCheckout(APIView):

    def post(self, request):
        for item in request.data:

            order = Order.objects.get(pk=item["order_id"])
            location_inventory_item = PencilBoxLocationInventoryItem.objects.get(pk=item["item_id"])

            location_inventory_item.in_stock -= item["qty"]
            location_inventory_item.save()

            order.fulfilled_at = timezone.now()
            order.save()

            item_value = location_inventory_item.inventory_item.value
            total_value = item_value * item["qty"]

            PencilBoxLocationInventoryItemOrder.objects.create(
              order=order,
              PencilBoxLocationInventoryItem=location_inventory_item,
              qty=item["qty"],
              value=total_value
            )

        payload_data = {
          "EMAIL": order.teacher.email,
          "NAME": order.teacher.first_name
        }
        thank_you_message = CourierMessage(
          'thank_you_message_payload',
          payload_data=payload_data,
          message_type='thanks'
        )
        thank_you_message.send_courier_message()
        return Response({"message": "CHECKOUT_SUCCESS"}, status=status.HTTP_201_CREATED)
