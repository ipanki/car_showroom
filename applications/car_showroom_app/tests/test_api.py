from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from applications.car_showroom_app.models import Showroom, Location


class PageApiUserTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser1', password='testpassword')
        cls.location = Location.objects.create(country='1', city='test2', street='test3', home='4')

    def setUp(self):
        self.client.login(username='testuser1', password='testpassword')

    def test_create_showroom(self):
        url = reverse('showroom-list')
        data = {'name': 'test', 'description': 'test1', 'location': self.location.pk}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Showroom.objects.count(), 1)
