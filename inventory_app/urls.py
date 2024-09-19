from django.urls import path
from admin_app.admin import admin_site
from admin_app.views.shopping_views import StartShop, TeacherCheckout, CancelCheckout, inventory_items
from admin_app.views.scheduling_views import ScheduleList, ScheduleRetrieve, SchoolList, RegisterNewTeacherForScheduleItem, RegisterTeacherForScheduleItem

APP_NAME = 'api'

urlpatterns = [
    path('admin/', admin_site.urls),
    path(f'{APP_NAME}/shopping/start/<int:teacher_schedule_item_id>', StartShop.as_view(), name='start-shopping'),
    path(f'{APP_NAME}/schedules', ScheduleList.as_view()),
    path(f'{APP_NAME}/shopping/cancel/<int:teacher_schedule_item_id>', CancelCheckout.as_view(), name='cancel_reservation'),
    path(f'{APP_NAME}/inventory_items/<int:location_id>', inventory_items, name='inventory_items')
    path(f'{APP_NAME}/schedules/<int:pk>', ScheduleRetrieve.as_view(), name='schedule_by_id'),
    path(f'{APP_NAME}/schools', SchoolList.as_view(),name='schools', name='available_schedules'),
    path(f'{APP_NAME}/schedules/<int:schedule_item_id>/slot_register', RegisterTeacherForScheduleItem.as_view(), name='slot_register'),
    path(f'{APP_NAME}/schedules/<int:schedule_item_id>/new_teacher', RegisterNewTeacherForScheduleItem.as_view(), name='new-teacher'),
    path(f'{APP_NAME}/shopping/checkout', TeacherCheckout.as_view(), name='checkout')
]
