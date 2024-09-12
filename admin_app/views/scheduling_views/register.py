from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from admin_app.models import ScheduleItem, Teacher, Order, PencilBoxLocation

class RegisterTeacherScheduleItem(APIView):
    def post(self, request, pk):
        email = request.data["email"]
        school = request.data["school_id"]
        
        try:
            teacher = Teacher.objects.get(email=email)
            schedule_item = ScheduleItem.objects.get(pk=pk)
            
            
        
        except (Teacher.DoesNotExist, ScheduleItem.DoesNotExist):
