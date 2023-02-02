from django.test import TestCase
from django.contrib.auth.models import User
from applications.car.models import CarConfiguration, Car
from applications.car_showroom_app.models import Showroom, CarsShowroom, Location


class ShowroomModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.user.save()
        cls.location = Location.objects.create(country='1', city='test2', street='test3', home='4')
        cls.location.save()
        cls.car_config = CarConfiguration.objects.create(
            description='test', color='Red', mileage=150, year=2020, engine=3.0, vin_number='1KLBN52TWXM186222')
        cls.car_config.save()
        cls.car = Car.objects.create(brand="Tes1", model="Test2", car=cls.car_config)

    def test_create_showroom(self):
        showroom = Showroom.objects.create(
            user=self.user, name='TestName', description="TestDescription", location=self.location)
        showroom.save()
        self.assertEqual(showroom.user, self.user)
        self.assertEqual(showroom.name, 'TestName')
        self.assertEqual(showroom.description, 'TestDescription')
        self.assertEqual(showroom.location, self.location)

    def test_create_car_showroom(self):
        showroom = Showroom.objects.create(
            user=self.user, name='TestName', description="TestDescription", location=self.location)
        car_showroom = CarsShowroom.objects.create(count=1, cars_showroom=self.car, car_showroom=showroom)
        car_showroom.save()
        self.assertEqual(car_showroom.count, 1)
        self.assertEqual(car_showroom.car_showroom, showroom)
        self.assertEqual(car_showroom.cars_showroom, self.car)
