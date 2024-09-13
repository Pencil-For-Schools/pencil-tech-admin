from admin_app.models import TeacherScheduleItem
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponseBadRequest


@api_view(['DELETE'])
def cancel_checkout(request, teacher_schedule_item_id):
    try:

        schedule_item = TeacherScheduleItem.objects.get(pk=teacher_schedule_item_id)


        if schedule_item:
            schedule_item.delete()
            return Response({'message': 'RESERVATION_CANCELLED'})

    except TeacherScheduleItem.DoesNotExist:
        return HttpResponseBadRequest("I could not find a schedule item.")

    except Exception as e:
        return HttpResponseBadRequest(str(e))


    return HttpResponseBadRequest("No valid action performed.")
