import unittest
from datetime import datetime
from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


def test_car(car_class, last_service_years_ago, current_mileage, last_service_mileage, warning_light_is_on):
    today = datetime.today().date()
    last_service_date = today.replace(year=today.year - last_service_years_ago)
    car = car_class(last_service_date, current_mileage, last_service_mileage, warning_light_is_on)
    return car.needs_service()


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        self.assertTrue(test_car(Calliope, 3, 0, 0, False))

    def test_battery_should_not_be_serviced(self):
        self.assertFalse(test_car(Calliope, 1, 0, 0, False))

    def test_engine_should_be_serviced(self):
        self.assertTrue(test_car(Calliope, 0, 30001, 0, False))

    def test_engine_should_not_be_serviced(self):
        self.assertFalse(test_car(Calliope, 0, 30000, 0, False))


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        self.assertTrue(test_car(Glissade, 3, 0, 0, False))

    def test_battery_should_not_be_serviced(self):
        self.assertFalse(test_car(Glissade, 1, 0, 0, False))

    def test_engine_should_be_serviced(self):
        self.assertTrue(test_car(Glissade, 0, 60001, 0, False))

    def test_engine_should_not_be_serviced(self):
        self.assertFalse(test_car(Glissade, 0, 60000, 0, False))


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        self.assertTrue(test_car(Palindrome, 5, 0, 0, False))

    def test_battery_should_not_be_serviced(self):
        self.assertFalse(test_car(Palindrome, 3, 0, 0, False))

    def test_engine_should_be_serviced(self):
        self.assertTrue(test_car(Palindrome, 0, 0, 0, True))

    def test_engine_should_not_be_serviced(self):
        self.assertFalse(test_car(Palindrome, 0, 0, 0, False))


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        self.assertTrue(test_car(Rorschach, 5, 0, 0, False))

    def test_battery_should_not_be_serviced(self):
        self.assertFalse(test_car(Rorschach, 3, 0, 0, False))

    def test_engine_should_be_serviced(self):
        self.assertTrue(test_car(Rorschach, 0, 60001, 0, False))

    def test_engine_should_not_be_serviced(self):
        self.assertFalse(test_car(Rorschach, 0, 60000, 0, False))
