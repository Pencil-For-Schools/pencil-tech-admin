from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from admin_app.models import ScheduleItem, Teacher, TeacherScheduleItem, School
from admin_app.utils import format_date_time, format_pencil_box_location
from integrations.courier.resources.courier_messages.courier_message import CourierMessage


class RegisterTeacherScheduleItemHelperView(APIView):
    def send_courier_messages(self, schedule_item, teacher):
        date, time = format_date_time(schedule_item.date_time)
        FORMATTED_TIME_TO_NOTIFY = "2 minutes"

        payload = {
            "EMAIL": teacher.email,
            "NAME": teacher.first_name + teacher.last_name,
            "DATE": date,
            "TIME": time,
            "LOC_NAME": schedule_item.pencil_box_location.name,
            "LOC_ADDRESS": format_pencil_box_location(
                schedule_item.pencil_box_location),
            "CANCEL_URL": "http://www.google.com",
            "TIME_TO_NOTIFY": FORMATTED_TIME_TO_NOTIFY
        }

        confirmation_message = CourierMessage(
            'confirmation_message_payload', payload_data=payload, message_type='confirmation')
        confirmation_message.send_courier_message()
        reminder_message = CourierMessage(
            'reminder_message_payload', payload_data=payload, message_type='reminder')
        reminder_message.send_courier_automation()


class RegisterNewTeacherForScheduleItem(RegisterTeacherScheduleItemHelperView):

    def post(self, request, schedule_item_id):
        teacher = Teacher.objects.get(pk=request.data["teacher_id"])
        schedule_item = ScheduleItem.objects.get(pk=schedule_item_id)

        teacher.first_name = request.data["first_name"]
        teacher.last_name = request.data["last_name"]
        teacher.phone = request.data["phone"]
        teacher.save()

        TeacherScheduleItem.objects.create(
            teacher=teacher,
            schedule_item=schedule_item
        )

        # self.send_courier_messages(schedule_item=schedule_item, teacher=teacher)

        response = {
            "message": "SUCCESSFUL_SCHEDULE_REGISTRATION",
            "teacher_id": teacher.id
        }

        return Response(response, status=status.HTTP_200_OK)


class RegisterTeacherForScheduleItem(RegisterTeacherScheduleItemHelperView):

    def post(self, request, schedule_item_id):
        email = request.data["email"]
        school_id = request.data["school_id"]

        response = {}

        teacher = None
        school = None
        schedule_item = None

        try:
            teacher = Teacher.objects.get(email=email)
        except Teacher.DoesNotExist:
            pass

        try:
            school = School.objects.get(pk=school_id)
        except School.DoesNotExist:
            response["message"] = "SCHOOL_INVALID"
            response["school_id"] = school_id
            return Response(response, status=status.HTTP_200_OK)

        try:
            schedule_item = ScheduleItem.objects.get(pk=schedule_item_id)
        except ScheduleItem.DoesNotExist:
            response["message"] = "SCHEDULE_ITEM_INVALID"
            response["schedule_item_id"] = schedule_item_id
            return Response(response, status=status.HTTP_200_OK)

        if teacher:
            TeacherScheduleItem.objects.create(
                teacher=teacher,
                schedule_item=schedule_item
            )
            # self.send_courier_messages(schedule_item=schedule_item, teacher=teacher)
            response = {
                "message": "SUCCESSFUL_SCHEDULE_REGISTRATION",
                "teacher_id": teacher.id
            }
        else:
            teacher = Teacher.objects.create(
                school=school,
                email=email,
            )
            response = {
                "message": "TEACHER_NOT_YET_REGISTERED",
                "shool_id": school_id,
                "email": email,
                "schedule_item_id": schedule_item_id,
                "teacher_id": teacher.id
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(response, status=status.HTTP_200_OK)
