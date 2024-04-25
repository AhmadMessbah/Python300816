from model.entity.base import Base


class Person(Base):
    def __init__(self, name, family):
        self.id = None
        self.name = name
        self.family = family






