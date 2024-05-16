from model.entity.base import Base
from model.tools.validator import Validator



class DrivingLicense(Base):
    def __init__(self, serial_number, date ,city , expire_date, person=None):
        self.id = None
        self.serial_number = serial_number
        self.date = date
        self.city= city
        self.expire_date= expire_date
        self.person = person

    def get_serial_number(self):
        return self._serial_number
    
    def set_serial_number(self, serial_number):
        self._serial_number =  Validator.serial_validator(serial_number, "Invalid Serial Number")
    
    def get_date(self):
        return self._date
    
    def set_date(self, date):
        self._date =  date
    
    def get_city(self):
        return self._city
    
    def set_city(self, city):
        self._city =  city
    
    def get_expire_date(self):
        return self._expire_date
    
    def set_expire_date(self, expire_date):
        self._expire_date =  expire_date
    
    def get_person(self):
        return self._person
    
    def set_person(self, person):
        self._person = person

    serial_number = property(get_serial_number, set_serial_number)
    date = property(get_date, set_date)
    city = property(get_city, set_city)
    expire_date = property(get_expire_date, set_expire_date)
    person = property(get_person, set_person)
