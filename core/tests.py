from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import MeetingRoom, Reservation
from django.contrib.auth.models import User
from rest_framework.test import APIClient


# Create your tests here.

class TestListRoomReservations(APITestCase):

    def setUp(self):
        self.client = APIClient(enforce_csrf_checks=True)

    def setUpTestData():
        user = User(email="test@test.com", username="testuser1", password = "testpasss")
        user.save()

        room = MeetingRoom(created_by = user)
        room.save()



    def test_get_reservation(self):
        self.client.login(username = "testuser1", password="testpass")

        url = reverse('list_room_reservations',kwargs = {'room_id':1})
        data = {
        "invitees":[1],
        "title":"Test Title",
        "reserved_from":"23/06/2021, 15:00",
        "reserved_to":"23/06/2021, 16:00",
        "room":1
        }

        response = self.client.get(url, data, format='json')
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_existing_reservations(self):
        pass

    def test_raise_error_when_try_to_book_booked_slot(self):
        pass


class UpdateReservation(APITestCase):

    def test_update_reservation(self):
        pass
