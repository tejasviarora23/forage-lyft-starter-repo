from datetime import datetime
from engine import CapuletEngine, WilloughbyEngine, SternmanEngine


def engine_class_with_service_threshold(engine_class, years):
    class NewEngine(engine_class):
        def needs_service(self):
            service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + years)
            if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
                return True
            else:
                return False
    return NewEngine


class Calliope(engine_class_with_service_threshold(CapuletEngine, 2)):
    pass


class Glissade(engine_class_with_service_threshold(WilloughbyEngine, 2)):
    pass


class Palindrome(engine_class_with_service_threshold(SternmanEngine, 4)):
    pass


class Rorschach(engine_class_with_service_threshold(WilloughbyEngine, 4)):
    pass
