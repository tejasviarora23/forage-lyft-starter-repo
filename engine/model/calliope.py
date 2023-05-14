from datetime import datetime, timedelta
from engine.capulet_engine import CapuletEngine

class Calliope(CapuletEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date + timedelta(days=365*2)
        return service_threshold_date < datetime.today().date() or self.engine_should_be_serviced()
