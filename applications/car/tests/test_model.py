from django.test import TestCase
from applications.car.models import CarConfiguration, Car, CarPrice


class CarModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.car_config = CarConfiguration.objects.create(
            description='test', color='Red', mileage=150, year=2020, engine=3.0, vin_number='1KLBN52TWXM186222')
        cls.car_config.save()
        cls.car = Car.objects.create(brand="Tes1", model="Test2", car=cls.car_config)

    def test_set_car_price(self):
        car_price = CarPrice.objects.create(car=self.car, price=12000)
        car_price.save()
        self.assertEqual(car_price.price, 12000)
        self.assertEqual(car_price.car, self.car)
