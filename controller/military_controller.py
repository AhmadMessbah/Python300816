from model.da.military_da import MilitaryDa
from model.da.person_da import PersonDa
from model.entity.military import Military
from model.tools.decorators import exception_handling
# from model.tools.logging import Logger


class MilitaryController:
    military_da = MilitaryDa()
    person_da = PersonDa()

    @classmethod
    @exception_handling
    def save(cls, serial_number, city, organ, start_year, start_month, start_day, end_year, end_month, end_day, soldier_id):
        if soldier_id:
            # Person-Connect
            soldier = cls.person_da.find_by_id(int(soldier_id))
            military = Military(serial_number,
                                city,
                                organ,
                                (int(start_year), int(start_month), int(start_day)),
                                (int(end_year), int(end_month), int(end_day)),
                                int(soldier))
        else:
            military = Military(serial_number,
                                city,
                                organ,
                                (int(start_year), int(start_month), int(start_day)),
                                (int(end_year), int(end_month), int(end_day)))
        cls.military_da.save(military)
        return True, f"Record saved successfully {military}"

    @classmethod
    @exception_handling
    def edit(cls, military_id, serial_number, city, organ,start_year, start_month, start_day, end_year, end_month, end_day, soldier_id):
        #Person-Connect
        soldier = cls.person_da.find_by_id(int(soldier_id))
        military = Military(serial_number,
                            city,
                            organ,
                            (int(start_year), int(start_month), int(start_day)),
                            (int(end_year), int(end_month), int(end_day)),
                            int(soldier))
        military.military_id = military_id
        old_military = cls.military_da.find_by_military_id(military_id)
        cls.military_da.edit(military)
        return True, (f"Record edited successfullyFrom : {old_military}\nTo: {military}")

    @classmethod
    @exception_handling
    def remove(cls, person_id):
        military = cls.military_da.find_by_military_id(person_id)
        cls.military_da.remove(person_id)
        return True, f"Record removed successfully {military}"

    @classmethod
    @exception_handling
    def find_all(cls, person_da=PersonDa()):
        return True, cls.military_da.find_all(person_da)

    @classmethod
    @exception_handling
    def find_by_military_id(cls, military_id, person_da=PersonDa()):
        return True, cls.military_da.find_by_military_id(military_id, person_da)

    @classmethod
    @exception_handling
    def find_by_serial_number(cls, serial_number, person_da=PersonDa()):
        return True, cls.military_da.find_by_serial_number(serial_number, person_da)

    @classmethod
    @exception_handling
    def find_by_organ(cls, organ, person_da=PersonDa()):
        return True, cls.military_da.find_by_organ(organ, person_da)

    @classmethod
    @exception_handling
    def find_by_city(cls, city, person_da):
        return True, cls.military_da.find_by_city(city, person_da=PersonDa())

    def find_by_soldier_id(cls, soldier_id, person_da):
        return True, cls.military_da.find_by_soldier_id(soldier_id, person_da=PersonDa())


