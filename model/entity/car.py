from model.entity.base import Base
from model.tools.validator import Validator



class Car(Base):
    def __init__(self, model, car_brand, color, owner=None):
        self.car_id = None
        self.model = model
        self.car_brand = car_brand
        self.color = color
        self.owner = owner

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = Validator.model_validator(model, "Invalid car model")

    def get_car_brand(self):
        return self._car_brand

    def set_car_brand(self, car_brand):
        self._car_brand = Validator.car_brand_validator(car_brand, "Invalid Brand")

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = Validator.color_validator(color, "Invalid Color")

    def get_owner(self):
        return self._owner

    def set_owner(self, owner):
        self._owner = owner

    model = property(get_model, set_model)
    car_brand = property(get_car_brand, set_car_brand)
    color = property(get_color, set_color)
    owner = property(get_owner, set_owner)
