from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from admin_app.models import TeacherScheduleItem
from integrations.courier.resources.courier_messages.courier_message import CourierMessage

class CancelCheckout(APIView):
    def post(self, teacher_schedule_item_id)
        try:
            teacher_schedule_item = TeacherScheduleItem.objects.get(pk=teacher_schedule_item_id)
            if teacher_schedule_item.order is None:
                message_payload = {
                    "name": teacher_schedule_item.teacher.first_name,
                    "email": teacher_schedule_item.teacher.email
                }
                cancel_message = CourierMessage(
                    'cancel_message_payload',
                    payload_data=message_payload,
                    message_type='cancel'
                )
                cancel_message.send_courier_message()
                teacher_schedule_item.delete()
                return Response({'message': 'RESERVATION_CANCELLED'})
        except TeacherScheduleItem.DoesNotExist:
            return Response({"message": "NO_SCHEDULED_SHOP"}, status=status.HTTP_400_BAD_REQUEST)
