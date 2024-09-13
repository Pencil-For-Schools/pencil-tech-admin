from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from admin_app.models import ScheduleItem, Teacher, TeacherScheduleItem, School
from admin_app.utils import format_date_time, format_pencil_box_location
from integrations.courier.resources.courier_messages.courier_message import CourierMessage

class RegisterTeacherScheduleItem(APIView):
    def send_courier_messages(self, payload):
        confirmation_message = CourierMessage('confirmation_message_payload', payload_data=payload, message_type='confirmation')
        confirmation_message.send_courier_message()
        reminder_message = CourierMessage('reminder_message_payload', payload_data=payload, message_type='reminder')
        reminder_message.send_courier_automation()

    def post(self, request, pk):
        email = request.data["email"]
        school_id = request.data["school_id"]

        try:
            if request.data["teacher_id"]:
                teacher = Teacher.objects.get(pk=request.data["teacher_id"])
                teacher.first_name = request.data["first_name"]
                teacher.last_name = request.data["last_name"]
                teacher.phone = request.data["phone"]
                teacher.save()
            else:
                teacher = Teacher.objects.get(email=email)
            schedule_item = ScheduleItem.objects.get(pk=pk)
            TeacherScheduleItem.objects.create(
              teacher=teacher,
              schedule_item=schedule_item
            )
            date, time = format_date_time(schedule_item.date_time)
            address = format_pencil_box_location(schedule_item.pencil_box_location)
            formatted_time_to_notify = "2 minutes"
            payload_data = {
              "EMAIL": email,
              "NAME": teacher.first_name + teacher.last_name,
              "DATE": date,
              "TIME": time,
              "LOC_NAME": schedule_item.pencil_box_location.name,
              "LOC_ADDRESS": address,
              "CANCEL_URL": "http://www.google.com",
              "TIME_TO_NOTIFY": formatted_time_to_notify
            }
            self.send_courier_messages(payload=payload_data)
            response = {
              "message": "SUCCESSFUL_SCHEDULE_REGISTRATION",
              "teacher_id": teacher.id
            }
            return Response(response, status=status.HTTP_200_OK)

        except Teacher.DoesNotExist:
            school = School.objects.get(pk=school_id)
            schedule_item = ScheduleItem.objects.get(pk=pk)
            teacher = Teacher.objects.create(
              school=school,
              email=email,
            )
            response = {
              "message": "TEACHER_NOT_YET_REGISTERED",
              "shool_id": school_id,
              "email": email,
              "schedule_item_id": pk,
              "teacher_id": teacher.id
            }
            return Response(response, status=status.HTTP_201_CREATED)
