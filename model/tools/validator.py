import re
from datetime import datetime


class Validator:
    def name_validator(self, name, message):
        if re.match(r"^[a-zA-Z\s]{2,30}$", name):
            return name
        else:
            raise ValueError(message)

    def date_validator(self, year, month, day, message):
        try:
            return datetime(year, month, day)
        except:
            raise ValueError(message)

    def date_time_validator(self, year, month, day, hour, minute, second, message):
        try:
            return datetime(year, month, day, hour, minute, second)
        except:
            raise ValueError(message)

    def amount_validator(self, amount, message):
        if isinstance(amount, int) and amount > 0:
            return amount
        else:
            raise ValueError(message)

    def doc_type_validator(self, doc_type, message):
        if doc_type in ("income", "outcome"):
            return doc_type
        else:
            raise ValueError(message)

    def grade_validator(self, grade, message):
        if re.match(r"^[a-zA-Z\s]{2,15}$", grade):
            return grade
        else:
            raise ValueError(message)

    def number_validator(self, number, message):
        if re.match(r"^[0-9]{2,11}$", number):
            return number
        else:
            raise ValueError(message)

    def operator_validator(self, operator, message):
        if isinstance(operator, str) and operator in ("irancell", "mci", "rightel", "shatel"):
            return operator
        else:
            raise ValueError(message)

    def price_validator(self, price, message):
        if re.match(r"^[0-9]{2,11}$", price):
            return price
        else:
            raise ValueError(message)

    def owner_validator(self, owner, message):
        if re.match(r"^[a-zA-Z\s]{5,50}$", owner):
            return owner
        else:
            raise ValueError(message)
