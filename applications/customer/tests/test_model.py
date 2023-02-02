from django.test import TestCase
from django.contrib.auth.models import User
from applications.car_showroom_app.models import Location
from applications.customer.models import Customer


class CustomerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.user.save()
        cls.location = Location.objects.create(country='1', city='test2', street='test3', home='4')
        cls.location.save()

    def test_create_customer(self):
        customer = Customer.objects.create(
            user=self.user, name="TestName", phone='+375333577888', location=self.location)
        customer.save()
        self.assertEqual(customer.user, self.user)
        self.assertEqual(customer.name, 'TestName')
        self.assertEqual(customer.phone, '+375333577888')
        self.assertEqual(customer.location, self.location)
