from model.entity.base import Base


class DrivingLicense(Base):
    def __init__(self, serial_number, date ,city , expire_date):
        self.id = None
        self.serial_number = serial_number
        self.date = date
        self.city= city
        self.expire_date= expire_date