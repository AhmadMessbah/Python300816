from model.da.car_da import CarDa
from model.da.person_da import PersonDa
from model.entity.car import Car
from model.tools.decorators import exception_handling


class CarController:
    car_da = CarDa()
    person_da = PersonDa()

    @classmethod
    @exception_handling
    def save(cls, model, car_brand, color, owner_id):
        color = int(color)
        if owner_id:
            owner = cls.person_da.find_by_id(owner_id)
            car = Car(model, car_brand, color, owner)
        else:
            car = Car(model, car_brand, color)

        cls.car_da.save(car)
        return True, f"Car saved successfully\n{car}"

    @classmethod
    @exception_handling
    def edit(cls, car_id, model, car_brand, color, owner_id):
        color = int(color)
        owner = cls.person_da.find_by_id(owner_id)
        car = Car(model, car_brand, color, owner)
        car.car_id = car_id
        old_car = cls.car_da.find_by_id(car_id)
        cls.car_da.edit(car)
        return True, (f"Car edited successfully\nFrom : {old_car}\nTo: {car}")

    @classmethod
    @exception_handling
    def remove(cls, car_id):
        car_id= int(car_id)
        car = cls.car_da.find_by_id(car_id)
        cls.car_da.remove(car_id)
        return True, f"car removed successfully\n{car}"

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.car_da.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, car_id):
        return True, cls.car_da.find_by_id(car_id)

    @classmethod
    @exception_handling
    def find_by_owner_id(cls, owner_id):
        return True, cls.car_da.find_by_owner_id(owner_id)
