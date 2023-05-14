from abc import ABC, abstractmethod
from datetime import datetime


class Car(ABC):
    SERVICE_INTERVAL = None

    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def service_threshold_date(self):
        return self.last_service_date.replace(year=self.last_service_date.year + self.SERVICE_INTERVAL)

    def needs_service(self):
        if self.service_threshold_date() < datetime.today().date():
            return True
        else:
            return False
