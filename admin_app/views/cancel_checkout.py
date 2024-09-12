from admin_app.models import teacher_schedule_item
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponseBadRequest


@api_view(['DELETE'])
def checkout(request, teacher_schedule_item_id):
    try:

        schedule_item = teacher_schedule_item.objects.get(pk=teacher_schedule_item_id)


        if schedule_item.schedule_item is None:
            schedule_item.delete()
            return Response({'message': 'RESERVATION_CANCELLED'})

    except teacher_schedule_item.DoesNotExist:
        return HttpResponseBadRequest("I could not find a schedule item.")

    except Exception as e:
        return HttpResponseBadRequest(str(e))


    return HttpResponseBadRequest("No valid action performed.")
