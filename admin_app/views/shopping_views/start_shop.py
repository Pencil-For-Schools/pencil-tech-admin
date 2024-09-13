from datetime import datetime

import pytz
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from admin_app.models import (Order,
                              TeacherScheduleItem)


def get_current_date_time():
    utc = pytz.timezone('UTC')
    now = utc.localize(datetime.now())
    cst = pytz.timezone('America/Chicago')
    local_time = now.astimezone(cst)
    return local_time


class StartShop(APIView):
    def create_teacher_order(self, teacher_schedule_item):
        teacher = teacher_schedule_item.teacher
        order = Order.objects.create(
            teacher=teacher,
            school=teacher.school,
        )
        teacher_schedule_item.order = order
        teacher_schedule_item.save()
        return order

    def post(self, request, teacher_schedule_id):
        response = {"teacher_schedule_id": teacher_schedule_id}

        teacher_schedule_item = None
        if teacher_schedule_id is not None:
            try:
                teacher_schedule_item = TeacherScheduleItem.objects.get(
                    pk=teacher_schedule_id)
            except TeacherScheduleItem.DoesNotExist:
                response["message"] = "DOES_NOT_EXIST"
                return Response(response, status=status.HTTP_404_NOT_FOUND)

        if teacher_schedule_item.order and teacher_schedule_item.order.fullfilled_at is None:

            now = get_current_date_time()
            today = now.date()

            order_date = teacher_schedule_item.schedule_item.date_time.date()
            is_early = order_date > today
            is_late = order_date < today
            response = {
                "email": teacher_schedule_item.teacher.email,
                "first_name": teacher_schedule_item.teacher.first_name,
                "last_name": teacher_schedule_item.teacher.last_name,
            }

            if is_early:
                response["message"] = "TEACHER_IS_EARLY"
                return Response(response, status=status.HTTP_200_OK)
            elif is_late:
                response["message"] = "TEACHER_IS_LATE"
                return Response(response, status=status.HTTP_200_OK)

            if teacher_schedule_item.order:
                response["order_id"] = teacher_schedule_item.order.id
                response["location_id"] = teacher_schedule_item.schedule_item.pencil_box_location.id
                response["message"] = "ORDER_OPEN"
                return Response(response, status=status.HTTP_200_OK)
            elif teacher_schedule_item.order is None:
                self.create_teacher_order(teacher_schedule_item)
                response["order_id"] = teacher_schedule_item.order.id
                response["location_id"] = teacher_schedule_item.schedule_item.pencil_box_location.id
                response["message"] = "ORDER_CREATED"
                return Response(response, status=status.HTTP_201_CREATED)
        else:
            response["message"] = "ORDER_ALREADY_COMPLETED"
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(response)
