from model.entity.base import Base
from model.tools.validator import Validator


class SimCard(Base):
    def __init__(self, number, operator, price, owner):
        self.sim_card_id = None
        self.number = number
        self.operator = operator
        self.price = price
        self.owner = owner

    def get_number(self):
        return self._number

    def set_number(self, number):
        self._number = Validator.number_validator(number, "Invalid Number")

    def get_operator(self):
        return self._operator

    def set_operator(self, operator):
        self._operator = Validator.operator_validator(operator, "Invalid Operator")

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = Validator.price_validator(price, "Invalid Price")

    def get_owner(self):
        return self._owner

    def set_owner(self, owner):
        self._owner = Validator.owner_validator(owner, "Invalid Owner")

    number = property(get_number, set_number)
    operator = property(get_operator, set_operator)
    price = property(get_price, set_price)
    owner = property(get_owner, set_owner)
