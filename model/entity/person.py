from model.entity.base import Base
from model.tools.validator import Validator


class Person(Base):
    def __init__(self, name, family, birth_date):
        self.person_id = None
        self.name = name
        self.family = family
        self.birth_date = birth_date

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = Validator.name_validator(name, "Invalid Name")

    def get_family(self):
        return self._family

    def set_family(self, family):
        self._family = Validator.name_validator(family, "Invalid Family")

    name = property(get_name, set_name)
    family = property(get_family, set_family)
