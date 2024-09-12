from datetime import timedelta, datetime
from django.utils import timezone
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from admin_app.models import TeacherScheduleItem, Teacher, Order, PencilBoxLocation

class StartShop(APIView):
    def teacher_has_email(self, email):
        return Teacher.objects.filter(email=email).exists()

    def teacher_schedule_item(self, email, location):
        teacher = Teacher.objects.get(email=email)
        now = timezone.now()
        one_day_ahead = now + timedelta(days=1)
        return TeacherScheduleItem.objects.filter(schedule_item__date_time__lte=one_day_ahead, teacher=teacher, schedule_item__pencil_box_location=location).first()

    def teacher_has_open_order(self, teacher_schedule_item):
        return teacher_schedule_item.order is not None and teacher_schedule_item.order.fulfilled_at is None

    def teacher_needs_order_created(self, teacher_schedule_item):
        return teacher_schedule_item.order is None

    def create_teacher_order(self, email, teacher_schedule_item):
        teacher = Teacher.objects.get(email=email)
        order = Order.objects.create(
            teacher = teacher,
            school = teacher.school,
            created_at = timezone.now()
        )
        teacher_schedule_item.order = order
        teacher_schedule_item.save()
        return order

    def post(self, request):
        email = request.data.get('teacher_email', None)
        location_id = request.data.get('location_id', None)
        if location_id is not None:
            location = PencilBoxLocation.objects.get(pk=location_id)
        if self.teacher_has_email(email):
            teacher_schedule_item = self.teacher_schedule_item(email=email, location=location)
            if teacher_schedule_item:
                if self.teacher_has_open_order(teacher_schedule_item):
                    response = {
                        "order_id": teacher_schedule_item.order.id,
                        "location_id": location_id
                    }
                    response["message"] = "ORDER_OPEN"
                    return Response(response, status=status.HTTP_200_OK)
                elif self.teacher_needs_order_created(teacher_schedule_item):
                    order = self.create_teacher_order(email, teacher_schedule_item)
                    response = {
                        "order_id": order.id,
                        "location_id": location_id
                    }
                    response["message"] = "ORDER_CREATED"
                    return Response(response, status=status.HTTP_201_CREATED)
            response = {
                "message": "TEACHER_NOT_SCHEDULED",
                "email": email
            }
        else:
            response = {
                "message": "TEACHER_EMAIL_INVALID",
                "email": email
            }
        return Response(response)
            