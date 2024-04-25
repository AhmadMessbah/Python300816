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
