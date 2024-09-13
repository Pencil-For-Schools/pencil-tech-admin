# from datetime import datetime, timedelta

# from django.db.models import Q
from django.http import Http404
# from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from admin_app.models import (Order, PencilBoxLocation, Teacher,
                              TeacherScheduleItem)


class StartShop(APIView):

    def get_open_teacher_schedule_item(self, teacher, location):
        open_teacher_schedule_item = None

        teacher_schedules_by_location = TeacherScheduleItem.objects.filter(
            teacher=teacher, schedule_item__pencil_box_location=location)

        if teacher_schedules_by_location.exists():
            schedule_without_order = teacher_schedules_by_location.filter(
                order__isnull=True).first()

            schedule_with_unfullfilled_order = (
                teacher_schedules_by_location
                .filter(
                    order__isnull=False, order__fullfilled_at__isnull=True
                ).first())

            if schedule_without_order:
                open_teacher_schedule_item = schedule_without_order
            elif schedule_with_unfullfilled_order:
                open_teacher_schedule_item = schedule_with_unfullfilled_order

        return open_teacher_schedule_item

    def create_teacher_order(self, teacher, teacher_schedule_item):
        order = Order.objects.create(
            teacher=teacher,
            school=teacher.school,
        )
        teacher_schedule_item.order = order
        teacher_schedule_item.save()
        return order

    def post(self, request):
        response = {}
        email = request.data.get('teacher_email', None)
        location_id = request.data.get('location_id', None)
        if location_id is not None:
            try:
                location = PencilBoxLocation.objects.get(pk=location_id)
            except PencilBoxLocation.DoesNotExist:
                raise Http404(
                    "No PencilBoxLocation matches the given query. asdas")

        if email is not None:
            teacher = Teacher.objects.filter(email=email).first()

        if teacher:
            teacher_schedule_item = self.get_open_teacher_schedule_item(
                teacher=teacher, location=location)
            if teacher_schedule_item:
                # Check to see if it's too early or too late here

                if teacher_schedule_item.order:
                    response = {
                        "order_id": teacher_schedule_item.order.id,
                        "location_id": location_id
                    }
                    response["message"] = "ORDER_OPEN"
                    return Response(response, status=status.HTTP_200_OK)
                elif teacher_schedule_item.order is None:
                    order = self.create_teacher_order(
                        teacher, teacher_schedule_item)
                    response = {
                        "order_id": order.id,
                        "location_id": location_id
                    }
                    response["message"] = "ORDER_CREATED"
                    return Response(response, status=status.HTTP_201_CREATED)
            else:
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
