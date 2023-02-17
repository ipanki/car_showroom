from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from applications.customer.models import Customer


class PageApiUserTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser1', password='testpassword')

    def setUp(self):
        self.client.login(username='testuser1', password='testpassword')

    def test_create_customer(self):
        url = reverse('customer-list')
        data = {'name': 'test', 'phone': '+375333577888'}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
