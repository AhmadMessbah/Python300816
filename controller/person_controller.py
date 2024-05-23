from model.da.person_da import PersonDa
from model.entity.person import Person
from model.tools.decorators import exception_handling
from model.tools.logging import Logger


class PersonController:
    person_da = PersonDa()

    @classmethod
    @exception_handling
    def save(cls, name, family,birth_date):
        person = Person(name, family,birth_date)
        cls.person_da.save(person)
        return True, f"Person saved successfully {person}"

    @classmethod
    @exception_handling
    def edit(cls, person_id, name, family, birth_date):
        person = Person(name, family,birth_date)
        person.person_id = person_id
        old_person = cls.person_da.find_by_id(person_id)
        cls.person_da.edit(person)
        return True, (f"Person edited successfullyFrom : {old_person}\nTo: {person}")

    @classmethod
    @exception_handling
    def remove(cls, person_id):
        person = cls.person_da.find_by_id(person_id)
        cls.person_da.remove(person_id)
        return True, f"Person removed successfully {person}"

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.person_da.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, person_id):
        return True, cls.person_da.find_by_id(person_id)

    @classmethod
    @exception_handling
    def find_by_family(cls, family):
        return True, cls.person_da.find_by_family(family)
