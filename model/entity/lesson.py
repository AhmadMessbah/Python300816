from model.entity.base import Base
from model.tools.validator import Validator


class Lesson(Base):
    def __init__(self, name, grade, teacher, start_day):
        self.lesson_id = None
        self.name = name
        self.grade = grade
        self.teacher = teacher
        self.start_day = start_day


    def get_name(self):
        return self._name


    def set_name(self, name):
        self._name = Validator.name_validator(name, "Invalid Lesson Name")


    def get_grade(self):
        return self._grade


    def set_grade(self, grade):
        self._grade = grade


    def get_teacher(self):
        return self._teacher


    def set_teacher(self, teacher):
        self._teacher = Validator.name_validator(teacher, "Invalid Teacher Name")


    def get_start_day(self):
        return self._start_day


    def set_start_day(self, start_day):
        self._start_day = Validator.date_validator(start_day, "Invalid Date")


    name = property(get_name, set_name)
    family = property(get_grade, set_grade)
    grade = property(get_grade, set_grade)
    start_day = property(get_start_day, set_start_day)
