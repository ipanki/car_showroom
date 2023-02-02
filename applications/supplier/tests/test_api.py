from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from applications.supplier.models import Supplier


class PageApiUserTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser1', password='testpassword')

    def setUp(self):
        self.client.login(username='testuser1', password='testpassword')

    def test_create_supplier(self):
        url = reverse('supplier-list')
        data = {'name': 'test', 'description': 'test1', 'found_year': '2001-01-01'}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Supplier.objects.count(), 1)
