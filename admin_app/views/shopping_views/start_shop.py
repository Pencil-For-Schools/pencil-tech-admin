from datetime import datetime, timedelta

import pytz
# from django.db.models import Q
from django.http import Http404
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from admin_app.models import (Order, PencilBoxLocation, Teacher,
                              TeacherScheduleItem)


def get_current_date_time():
    utc = pytz.timezone('UTC')
    now = utc.localize(datetime.utcnow())
    cst = pytz.timezone('America/Chicago')
    local_time = now.astimezone(cst)
    return local_time
class StartShop(APIView):

    def get_open_teacher_schedule_item(self, teacher, location):
        open_teacher_schedule_item = None

        teacher_schedules_by_location = TeacherScheduleItem.objects.filter(
            teacher=teacher, schedule_item__pencil_box_location=location).order_by('-schedule_item__date_time')

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
        teacher_schedule_id = request.data.get('teacher_schedule_id', None)


        if teacher_schedule_id is not None:
            teacher_schedule_item = TeacherScheduleItem.objects.get(pk=teacher_schedule_id)
            # throw not found error

        if teacher_schedule_item:
            if teacher_schedule_item:
                now = get_current_date_time()
                today = now.date()

                order_date = teacher_schedule_item.schedule_item.date_time.date()
                is_early = order_date > today
                is_late = order_date < today

                if is_early:
                    response = {
                        "email": email,
                        "message": "TEACHER_IS_EARLY"
                    }
                    return Response(response, status=status.HTTP_200_OK)
                elif is_late:
                    response = {
                        "email": email,
                        "message": "TEACHER_IS_LATE"
                    }
                    response["message"] = "TEACHER_IS_LATE"
                    return Response(response, status=status.HTTP_200_OK)

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
