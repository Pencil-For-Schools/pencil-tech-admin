from django.urls import path
from admin_app.admin import admin_site
from admin_app.views.shopping_views import StartShop, CancelCheckout, inventory_items
from admin_app.views.scheduling_views import ScheduleList, ScheduleRetrieve, SchoolList, RegisterNewTeacherForScheduleItem, RegisterTeacherForScheduleItem

APP_NAME = 'api'

urlpatterns = [
    path('admin/', admin_site.urls),
    path(f'{APP_NAME}/shopping/start/<int:teacher_schedule_id>', StartShop.as_view()),
    path(f'{APP_NAME}/schedules', ScheduleList.as_view()),
    path(f'{APP_NAME}/schedules/<int:pk>', ScheduleRetrieve.as_view()),
    path(f'{APP_NAME}/schools', SchoolList.as_view()),
    path(f'{APP_NAME}/schedules/<int:schedule_item_id>/slot_register', RegisterTeacherForScheduleItem.as_view()),
    path(f'{APP_NAME}/schedules/<int:schedule_item_id>/new_teacher', RegisterNewTeacherForScheduleItem.as_view()),
    path(f'{APP_NAME}/shopping/cancel/<int:teacher_schedule_item_id>', CancelCheckout.as_view()),
    path(f'{APP_NAME}/shopping/inventory_items/<int:location_id>', inventory_items)
]
