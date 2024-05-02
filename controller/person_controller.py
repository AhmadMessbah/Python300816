from model.da.person_da import PersonDa
from model.entity.person import Person
from model.tools.decorators import exception_handling


class PersonController:
    person_da = PersonDa()

    @classmethod
    @exception_handling
    def save(cls, name, family):
        person = Person(name, family)
        cls.person_da.save(person)
        return True, f"Person saved successfully\n{person}"

    @exception_handling
    @classmethod
    def edit(cls, person_id, name, family):
        person = Person(name, family)
        person.person_id = person_id
        old_person = cls.person_da.find_by_id(person_id)
        cls.person_da.edit(person)
        return True, (f"Person edited successfully\nFrom : {old_person}\nTo: {person}")

    @exception_handling
    @classmethod
    def remove(cls, person_id):
        person = cls.person_da.find_by_id(person_id)
        cls.person_da.remove(person_id)
        return True, f"Person removed successfully\n{person}"

    @exception_handling
    @classmethod
    def find_all(cls):
        return True, cls.person_da.find_all()

    @exception_handling
    @classmethod
    def find_by_id(cls, person_id):
        return True, cls.person_da.find_by_id(person_id)

    @exception_handling
    @classmethod
    def find_by_family(cls, family):
        return True, cls.person_da.find_by_family(family)
