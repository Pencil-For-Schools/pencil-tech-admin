from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from admin_app.models import ScheduleItem, Teacher, TeacherScheduleItem, School
from admin_app.utils import format_date_time, format_pencil_box_location
from integrations.courier.resources.courier_messages.courier_message import CourierMessage

class TeacherRegister(APIView):
    def post(self, request, pk):
        try:
            teacher = Teacher.objects.get(email=email)
            teacher.first_name = request.data["first_name"]
            teacher.last_name = request.data["last_name"]
            teacher.phone = request.data["phone"]
            teacher.
            
            
        except Teacher.DoesNotExist:
