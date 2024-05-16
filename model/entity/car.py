from model.entity.base import Base
from model.tools.validator import Validator



class CaR(Base):
    def __init__(self, model, name, color, owner=None):
        self.card_id = None
        self.model = model
        self.name = name
        self.color = color
        self.owner = owner

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = Validator.phone_model_validator(model, "Invalid model")

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = Validator.name_validator(name, "Invalid name")

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = Validator.color_validator(color, "Invalid color")

    def get_owner(self):
        return self._owner

    def set_owner(self, owner):
        self._owner = owner

    model = property(get_model, set_model)
    name = property(get_name, set_name)
    color = property(get_color, set_color)
    owner = property(get_owner, set_owner)
