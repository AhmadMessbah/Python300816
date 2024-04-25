from model.entity.base import Base


class Person(Base):
    def __init__(self, name, family):
        self.person_id = None
        self.name = name
        self.family = family
