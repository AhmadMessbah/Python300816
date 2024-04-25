from model.da.da import Da
from model.entity.person import Person


class PersonDa(Da):
    def save(self, person):
        self.connect()
        self.cursor.execute("INSERT INTO PERSON_TBL(NAME, FAMILY) VALUES(%s,%s)",
                            [person.name, person.family])
        self.connection.commit()
        self.disconnect()

    def edit(self, person):
        self.connect()
        self.cursor.execute("UPDATE PERSON_TBL SET NAME=%s, FAMILY=%s WHERE ID=%s",
                            [person.name, person.family, person.person_id])
        self.connection.commit()
        self.disconnect()

    def remove(self, person_id):
        self.connect()
        self.cursor.execute("DELETE FROM PERSON_TBL WHERE ID=%s",
                            [person_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM PERSON_TBL")
        person_tuple_list = self.cursor.fetchall()
        self.disconnect()
        if person_tuple_list:
            person_list = []
            for person_tuple in person_tuple_list:
                person = Person(person_tuple[1], person_tuple[2])
                person.person_id = person_tuple[0]
                person_list.append(person)
            return person_list
        else:
            raise ValueError("No Person Found !")

    def find_by_id(self, person_id):
        self.connect()
        self.cursor.execute("SELECT * FROM PERSON_TBL WHERE ID=%s", [person_id])
        person_tuple = self.cursor.fetchone()
        self.disconnect()
        if person_tuple:
            person = Person(person_tuple[1], person_tuple[2])
            person.person_id = person_tuple[0]
            return person
        else:
            raise ValueError("No Person Found !")

    def find_by_family(self, family):
        self.connect()
        self.cursor.execute("SELECT * FROM PERSON_TBL WHERE FAMILY=%s", [family])
        person_tuple_list = self.cursor.fetchall()
        self.disconnect()
        if person_tuple_list:
            person_list = []
            for person_tuple in person_tuple_list:
                person = Person(person_tuple[1], person_tuple[2])
                person.person_id = person_tuple[0]
                person_list.append(person)
            return person_list
        else:
            raise ValueError("No Person Found !")
