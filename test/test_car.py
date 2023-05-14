import unittest
from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_carrigan_tires_should_be_serviced(self):
        tire_wear_array = [0.1, 0.2, 0.3, 0.9]

        car = Calliope()
        self.assertTrue(car.needs_tire_service('Carrigan', tire_wear_array))

    def test_carrigan_tires_should_not_be_serviced(self):
        tire_wear_array = [0.1, 0.2, 0.3, 0.8]

        car = Calliope()
        self.assertFalse(car.needs_tire_service('Carrigan', tire_wear_array))

    def test_octoprime_tires_should_be_serviced(self):
        tire_wear_array = [0.5, 0.5, 1.5, 0.5]

        car = Calliope()
        self.assertTrue(car.needs_tire_service('Octoprime', tire_wear_array))

    def test_octoprime_tires_should_not_be_serviced(self):
        tire_wear_array = [0.5, 0.5, 0.9, 0.5]

        car = Calliope()
        self.assertFalse(car.needs_tire_service('Octoprime', tire_wear_array))


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year
