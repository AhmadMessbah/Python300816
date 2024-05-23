from model.da.military_da import MilitaryDa
from model.da.person_da import PersonDa
from model.entity.military import Military
from model.tools.decorators import exception_handling


class MilitaryController:
    military_da = MilitaryDa()
    person_da = PersonDa()

    @classmethod
    @exception_handling
    def save(cls, serial_number, city, organ, start_date, end_date, soldier_id):
        if soldier_id:
            soldier = cls.person_da.find_by_id(int(soldier_id))
            military = Military(serial_number, city, organ, start_date, end_date, soldier)
        else:
            military = Military(serial_number, city, organ, start_date, end_date)

        cls.military_da.save(military)
        return True, f"Record saved successfully {military}"

    @classmethod
    @exception_handling
    def edit(cls, military_id, serial_number, city, organ, start_date, end_date, soldier_id):

        soldier = cls.person_da.find_by_id(int(soldier_id))
        military = Military(serial_number, city, organ, start_date, end_date, soldier)
        military.military_id = military_id
        old_military = cls.military_da.find_by_id(military_id)
        cls.military_da.edit(military)
        return True, f"Record edited successfullyFrom : {old_military}\nTo: {military}"

    @classmethod
    @exception_handling
    def remove(cls, person_id):
        military = cls.military_da.find_by_id(person_id)
        cls.military_da.remove(person_id)
        return True, f"Record removed successfully {military}"

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.military_da.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, military_id):
        return True, cls.military_da.find_by_id(military_id)

    @classmethod
    @exception_handling
    def find_by_person(cls, soldier_id):
        return True, cls.military_da.find_by_person(int(soldier_id))
