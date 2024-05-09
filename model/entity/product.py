from model.entity.base import Base
from model.tools.validator import Validator


class Product(Base):
    def __init__(self, name, brand, serial, buy_price, person = None):
        self.product_id = None
        self.name = name
        self.brand = brand
        self.serial = serial
        self.buy_price = buy_price
        self.person = person

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = Validator.name_validator(name, "Invalid Name")

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        self._brand = Validator.name_validator(brand, "Invalid Brand")

    def get_serial(self):
        return self._serial

    def set_serial(self, serial):
        self._serial = Validator.serial_validator(serial, "Invalid Serial")

    def get_buy_price(self):
        return self._price

    def set_buy_price(self, buy_price):
        self._price = Validator.buy_price_validator(buy_price, "Invalid Price")
    name = property(get_name, set_name)
    brand = property(get_brand, set_brand)
    serial = property(get_serial, set_serial)
    buy_price = property(get_buy_price, set_buy_price)
