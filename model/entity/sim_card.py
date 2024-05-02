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
        return self.set_number()

    def set_number(self, number):
        self._number = Validator.name_validator(number, "Invalid Number")

    def get_operator(self):
        return self._operator

    def set_operator(self, operator):
        self._operator = Validator.name_validator(operator, "Invalid Operator")

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = Validator.name_validator(price, "Invalid Price")

    def get_owner(self,owner):
        return self._owner

    def set_owner(self, owner):
        self._owner = Validator.name_validator(owner, "Invalid owner")


    number = property(get_number, set_number)
    oprator = property(get_oprator, set_oprator)
    price = property(get_price, set_price)
    owner = property(get_owner, set_owner)