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
        if doc_type.lower() in ("income", "outcome"):
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
    def brand_validator(cls, brand, message):
        if isinstance(brand, str) and brand.lower() in ("irancell", "mci", "rightel", "shatel"):
            return brand
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
        if re.match(r"^[\w@!#$%^&*\s]{2,16}$", password):
            return password
        else:
            raise ValueError(message)

    @classmethod
    def serial_validator(cls, serial_number, message):
        if isinstance(serial_number, str) and re.match(r"^\w{2,30}$", serial_number):
            return serial_number
        else:
            raise ValueError(message)

    @classmethod
    def car_brand_validator(cls, car_brand, message):
        if isinstance(car_brand, str) and car_brand.lower() in ("VOLVO", "BMW", "FORD", "HYUNDAI","JEEP","HONDA","FERRARI","TOYOTA","KIA","LEXUS","BENZ"):
            return car_brand
        else:
            raise ValueError(message)

    @classmethod
    def color_validator(cls, color, message):
        if re.match(r"^[a-zA-Z\s]", color):
            return color
        else:
            raise ValueError(message)

    @classmethod
    def model_validator(cls, model, message):
        if re.match(r"^[a-zA-Z\s]{2,15}$", model):
            return model
        else:
            raise ValueError(message)
