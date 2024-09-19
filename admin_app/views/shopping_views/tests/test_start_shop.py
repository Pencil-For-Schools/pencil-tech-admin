from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.utils import timezone
from admin_app.models import Teacher, TeacherScheduleItem, Order, PencilBoxLocation
from datetime import timedelta


# TODO
class StartShoppingTests(APITestCase):

    def setUp(self):
        # Set up some common test data
        self.teacher = Teacher.objects.create(
            email="teacher1@example.com",
            first_name="Teacher",
            last_name="One",
            school=None,  # You may need to adjust if a School instance is needed
            county=None,  # You may need to adjust if a County instance is needed
        )

        self.location = PencilBoxLocation.objects.create(name="Location 1", address1="123 Main St")
        self.location_id = self.location.id
        self.today = timezone.now().date()

        # Create teacher schedule items for different date scenarios
        self.early_schedule = TeacherScheduleItem.objects.create(
            teacher=self.teacher,
            schedule_item=None,  # Assuming this should link to a ScheduleItem
            order=None
        )
        self.late_schedule = TeacherScheduleItem.objects.create(
            teacher=self.teacher,
            schedule_item=None,
            order=None,
            schedule_date=self.today + timedelta(days=1)
        )
        self.today_schedule = TeacherScheduleItem.objects.create(
            teacher=self.teacher,
            schedule_item=None,
            order=None,
            schedule_date=self.today
        )

    def test_teacher_schedule_does_not_exist(self):
        # Test when the teacher schedule item does not exist
        response = self.client.post(reverse('start-shopping', kwargs={'teacher_schedule_id': 999}))  # Non-existent schedule
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['message'], "DOES_NOT_EXIST")
        self.assertEqual(response.data['schedule_id'], 999)

    def test_teacher_early(self):
        # Test when the teacher's schedule date is early
        response = self.client.post(reverse('start-shopping', kwargs={'teacher_schedule_id': self.early_schedule.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "TEACHER_EARLY")
        self.assertEqual(response.data['email'], self.teacher.email)
        self.assertEqual(response.data['first_name'], self.teacher.first_name)
        self.assertEqual(response.data['last_name'], self.teacher.last_name)

    def test_teacher_late(self):
        # Test when the teacher's schedule date is late
        response = self.client.post(reverse('start-shopping', kwargs={'teacher_schedule_id': self.late_schedule.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "TEACHER_LATE")
        self.assertEqual(response.data['email'], self.teacher.email)
        self.assertEqual(response.data['first_name'], self.teacher.first_name)
        self.assertEqual(response.data['last_name'], self.teacher.last_name)

    def test_teacher_on_time_order_open(self):
        # Test when the teacher is on time and has an open order
        order = Order.objects.create(teacher=self.teacher, school=None, pickup=False)  # Adjust as needed
        self.today_schedule.order = order
        self.today_schedule.save()

        response = self.client.post(reverse('start-shopping', kwargs={'teacher_schedule_id': self.today_schedule.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "ORDER_OPEN")
        self.assertEqual(response.data['order_id'], order.id)
        self.assertEqual(response.data['location_id'], self.location_id)

    def test_teacher_on_time_order_completed(self):
        # Test when the teacher is on time and the order is completed
        order = Order.objects.create(teacher=self.teacher, school=None, pickup=False, fulfilled_at=timezone.now())
        self.today_schedule.order = order
        self.today_schedule.save()

        response = self.client.post(reverse('start-shopping', kwargs={'teacher_schedule_id': self.today_schedule.id}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], "ORDER_COMPLETED")

    def test_teacher_on_time_create_order(self):
        # Test when the teacher is on time and the order needs to be created
        response = self.client.post(reverse('start-shopping', kwargs={'teacher_schedule_id': self.today_schedule.id}))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "ORDER_CREATED")
        self.assertIsNotNone(response.data['order_id'])
        self.assertEqual(response.data['location_id'], self.today_schedule.location_id)
