from django.test import TestCase
from django.contrib.auth.models import User
from applications.car.models import CarConfiguration, Car
from applications.supplier.models import Supplier, CarSupplier


class SupplierModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.user.save()
        cls.car_config = CarConfiguration.objects.create(
            description='test', color='Red', mileage=150, year=2020, engine=3.0, vin_number='1KLBN52TWXM186222')
        cls.car_config.save()
        cls.car = Car.objects.create(brand="Tes1", model="Test2", car=cls.car_config)

    def test_create_supplier(self):
        supplier = Supplier.objects.create(user=self.user, name='TestName', description="TestDescription", found_year='2001-01-01')
        supplier.save()
        self.assertEqual(supplier.user, self.user)
        self.assertEqual(supplier.name, 'TestName')
        self.assertEqual(supplier.description, 'TestDescription')
        self.assertEqual(supplier.found_year, '2001-01-01')

    def test_create_car_supplier(self):
        car_supplier = CarSupplier.objects.create(count=1, car=self.car)
        car_supplier.save()
        self.assertEqual(car_supplier.count, 1)
        self.assertEqual(car_supplier.car, self.car)
