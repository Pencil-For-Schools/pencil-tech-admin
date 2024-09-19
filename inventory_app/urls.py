"""
URL configuration for inventory_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from admin_app.admin import admin_site
from admin_app.views.shopping_views import StartShop, TeacherCheckout
from admin_app.views.scheduling_views import ScheduleList, ScheduleRetrieve, SchoolList, RegisterNewTeacherForScheduleItem, RegisterTeacherForScheduleItem

APP_NAME = 'api'

urlpatterns = [
    path('admin/', admin_site.urls),
    path(f'{APP_NAME}/shopping/start/<int:teacher_schedule_item_id>', StartShop.as_view(), name='start-shopping'),
    path(f'{APP_NAME}/schedules', ScheduleList.as_view()),
    path(f'{APP_NAME}/schedules/<int:pk>', ScheduleRetrieve.as_view(), name='schedule_by_id'),
    path(f'{APP_NAME}/schools', SchoolList.as_view(),name='schools', name='available_schedules'),
    path(f'{APP_NAME}/schedules/<int:schedule_item_id>/slot_register', RegisterTeacherForScheduleItem.as_view(), name='slot_register'),
    path(f'{APP_NAME}/schedules/<int:schedule_item_id>/new_teacher', RegisterNewTeacherForScheduleItem.as_view(), name='new-teacher'),
    path(f'{APP_NAME}/shopping/checkout', TeacherCheckout.as_view(), name='checkout')
    # path(f'{APP_NAME}/shopping/cancel/<int:teacher_schedule_item_id>', .as_view(), name='cancel_reservation')
    # path(f'{APP_NAME}/inventory_items/<int:location_id>', .as_view(), name='inventory_items')
]
