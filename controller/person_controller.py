from model.da.person_da import PersonDa
from model.entity.person import Person
from model.tools.validator import Validator


class PersonController:
    def __init__(self):
        self.validator = Validator()

    def save(self, name, family):
        try:
            person = Person(
                self.validator.name_validator(name, "Invalid Name"),
                self.validator.name_validator(family, "Invalid Family")
            )
            person_da = PersonDa()
            person_da.save(person)
            return True, f"Person saved successfully\n{person}"
        except Exception as e:
            return False, str(e)

    def edit(self, person_id, name, family):
        try:
            person = Person(
                self.validator.name_validator(name, "Invalid Name"),
                self.validator.name_validator(family, "Invalid Family")
            )
            person.person_id = person_id
            person_da = PersonDa()
            old_person = person_da.find_by_id(person_id)
            person_da.edit(person)
            return True, (f"Person edited successfully\nFrom : {old_person}\nTo: {person}")
        except Exception as e:
            return False, str(e)

    def remove(self, person_id):
        try:
            person_da = PersonDa()
            person = person_da.find_by_id(person_id)
            person_da.remove(person_id)
            return True, f"Person removed successfully\n{person}"
        except Exception as e:
            return False, str(e)

    def find_all(self):
        try:
            person_da = PersonDa()
            return True, person_da.find_all()
        except Exception as e:
            return False, str(e)

    def find_by_id(self, person_id):
        try:
            person_da = PersonDa()
            return True, person_da.find_by_id(person_id)
        except Exception as e:
            return False, str(e)

    def find_by_family(self, family):
        try:
            person_da = PersonDa()
            return True, person_da.find_by_family(
                self.validator.name_validator(family, "Invalid Family")
            )
        except Exception as e:
            return False, str(e)
