from model.entity.base import Base
from model.tools.validator import Validator


class Military(Base):
    def __init__(self, serial_number, city, organ, start_date, end_date):
        self.military_id = None
        self.serial_number = serial_number
        self.city = city
        self.organ = organ
        self.start_date = start_date
        self.end_date = end_date

    def get_serial_number(self):
        return self._serial_number

    def set_serial_number(self, serial_number):
        self._serial_number = Validator.serial_validator(serial_number, "Invalid Serial Number")

    def get_city(self):
        return self._city

    def set_city(self, city):
        self._city = Validator.name_validator(city, "Invalid City Name")

    def get_organ(self):
        return self._organ

    def set_organ(self, organ):
        self._organ = Validator.name_validator(organ, "Invalid Organ Name")

    def get_start_date(self):
        return self._start_date

    def set_start_date(self, start_date):
        self._start_date = Validator.date_validator(start_date, "Invalid Start Date")

    def get_end_date(self):
        return self._end_date

    def set_end_date(self, end_date):
        self._end_date = Validator.date_validator(end_date, "Invalid End Date")



    serial_number = property(get_serial_number , set_serial_number)
    city = property(get_city, set_city)
    organ = property(get_organ, set_organ)
    start_date = property(get_start_date, set_start_date)
    end_date = property(get_end_date, set_end_date)