import re
from datetime import datetime


class Lesson_validator:
    def name_validator(self, name, message):
        if re.match(r"^[a-zA-Z\s]{2,30}$", name):
            return name
        else:
            raise ValueError(message)

    def grade_validator(self, grade, message):
        if re.match(r"^[a-zA-Z\s]{2,15}$", grade):
            return grade
        else:
            raise ValueError(message)

    def date_validator(self, year, month, day, message):
        try:
            return datetime.date(year, month, day)
        except:
            raise ValueError(message)
