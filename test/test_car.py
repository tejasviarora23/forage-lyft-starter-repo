#unit test for the Car base class:

class TestCar(unittest.TestCase):
    def test_needs_service_raises_not_implemented_error(self):
        with self.assertRaises(NotImplementedError):
            car = Car(datetime.today().date())
            car.needs_service()

#unit test for the Thovex class:
class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        self.assertTrue(Thovex(datetime(2020, 1, 1), 0, 0, False).needs_service())

    def test_battery_should_not_be_serviced(self):
        self.assertFalse(Thovex(datetime(2022, 1, 1), 0, 0, False).needs_service())

    def test_engine_should_be_serviced(self):
        self.assertTrue(Thovex(datetime(2020, 1, 1), 60001, 0, False).needs_service())

    def test_engine_should_not_be_serviced(self):
        self.assertFalse(Thovex(datetime(2020, 1, 1), 60000, 0, False).needs_service())
