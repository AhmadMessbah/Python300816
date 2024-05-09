import re
from datetime import datetime,date


class Validator:
    @classmethod
    def name_validator(cls, name, message):
        if isinstance(name, str) and re.match(r"^[a-zA-Z\s]{2,30}$", name):
            return name
        else:
            raise ValueError(message)

    @classmethod
    def date_validator(cls, date_tuple, message):
        if isinstance(date_tuple, date):
            return date_tuple
        try:
            return datetime(*date_tuple).date()
        except:
            raise ValueError(message)

    @classmethod
    def date_time_validator(cls, year, month, day, hour, minute, second, message):
        try:
            return datetime(year, month, day, hour, minute, second)
        except:
            raise ValueError(message)

    @classmethod
    def amount_validator(cls, amount, message):
        if isinstance(amount, int) and amount > 0:
            return amount
        else:
            raise ValueError(message)

    @classmethod
    def doc_type_validator(cls, doc_type, message):
        if doc_type in ("income", "outcome"):
            return doc_type
        else:
            raise ValueError(message)

    @classmethod
    def grade_validator(cls, grade, message):
        if re.match(r"^[a-zA-Z\s]{2,15}$", grade):
            return grade
        else:
            raise ValueError(message)

    @classmethod
    def phone_number_validator(cls, number, message):
        if re.match(r"^(09|\+989)\d{9}$", number):
            return number
        else:
            raise ValueError(message)

    @classmethod
    def operator_validator(cls, operator, message):
        if isinstance(operator, str) and operator.lower() in ("irancell", "mci", "rightel", "shatel"):
            return operator
        else:
            raise ValueError(message)

    @classmethod
    def price_validator(cls, price, message):
        if isinstance(price, int) and price >= 0:
            return price
        else:
            raise ValueError(message)

    @classmethod
    def owner_validator(cls, owner, message):
        if re.match(r"^[a-zA-Z\s]{5,50}$", owner):
            return owner
        else:
            raise ValueError(message)


    @classmethod
    def username_validator(cls, username, message):
        if re.match(r"^[\w@!#$%^&*\s]{2,30}$", username):
            return username
        else:
            raise ValueError(message)

    @classmethod
    def password_validator(cls, password, message):
        if re.match(r"^[\w@!#$%^&*\s]{8,16}$", password):
            return password
        else:
            raise ValueError(message)

    @classmethod
    def serial_validator(cls, serial_number, message):
        if isinstance(serial_number, str) and re.match(r"^[0-9]{11}$", serial_number):
            return serial_number
        else:
            raise ValueError(message)