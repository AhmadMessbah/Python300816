from model.da.da import Da
from model.entity.user import User
from model.da.person_da import PersonDa


class UserDa(Da):
    def save(self, user):
        self.connect()
        self.cursor.execute("INSERT INTO USER_TBL(USERNAME, PASSWORD, STATUS, LOCKED , PERSON_ID) VALUES(%s,%s,%s,%s,%s)",
                            [user.username,
                             user.password,
                             user.status,
                             user.locked,
                             user.person.person_id if user.person else None])
        self.connection.commit()
        self.disconnect()

    def edit(self, user):
        self.connect()
        self.cursor.execute("UPDATE USER_TBL SET USERNAME=%s, PASSWORD=%s, STATUS=%s, LOCKED=%s , PERSON_ID=%s  WHERE ID=%s",
                            [user.username,
                             user.password,
                             user.status,
                             user.locked,
                             user.user_id,
                             user.person.person_id if user.person else None
                             ])
        self.connection.commit()
        self.disconnect()

    def remove(self, user_id):
        self.connect()
        self.cursor.execute("DELETE FROM USER_TBL WHERE ID=%s",
                            [user_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM USER_TBL")
        user_tuple_list = self.cursor.fetchall()
        self.disconnect()
        person_da = PersonDa()
        if user_tuple_list:
            user_list = []
            for user_tuple in user_tuple_list:
                user = User(user_tuple[1], user_tuple[2])
                user.user_id = user_tuple[0]
                user.status = user_tuple[3]
                user.locked = user_tuple[4]
                user.person = person_da.find_by_id(user_tuple[5])
                user_list.append(user)
            return user_list
        else:
            raise ValueError("No User Found !")

    def find_by_id(self, user_id):
        self.connect()
        self.cursor.execute("SELECT * FROM USER_TBL WHERE ID=%s", [user_id])
        user_tuple = self.cursor.fetchone()
        self.disconnect()
        person_da = PersonDa()
        if user_tuple:
            user = User(user_tuple[1], user_tuple[2])
            user.user_id = user_tuple[0]
            user.status = user_tuple[3]
            user.locked = user_tuple[4]
            user.person = person_da.find_by_id(user_tuple[5])
            person_da.find_by_id(user_tuple[5])
            return user
        else:
            raise ValueError("No User Found !")

    def find_by_username(self, username):
        self.connect()
        self.cursor.execute("SELECT * FROM USER_TBL WHERE USERNAME LIKE %s", [username +"%"])
        user_tuple_list = self.cursor.fetchall()
        self.disconnect()
        person_da = PersonDa()
        if user_tuple_list:
            user_list = []
            for user_tuple in user_tuple_list:
                user = User(user_tuple[1], user_tuple[2])
                user.user_id = user_tuple[0]
                user.status = user_tuple[3]
                user.locked = user_tuple[4]
                user.person = person_da.find_by_id(user_tuple[5])
                user_list.append(user)
            return user_list
        else:
            raise ValueError("No User Found !")

    def find_by_person_id(self, person_id):
        self.connect()
        self.cursor.execute("SELECT * FROM USER_TBL WHERE PERSON_ID=%s", [person_id])
        user_tuple_list = self.cursor.fetchall()
        self.disconnect()
        person_da = PersonDa()
        if user_tuple_list:
            user_list = []
            for user_tuple in user_tuple_list:
                user = User(user_tuple[1], user_tuple[2])
                user.user_id = user_tuple[0]
                user.status = user_tuple[3]
                user.locked = user_tuple[4]
                user.person = person_da.find_by_id(user_tuple[5])
                user_list.append(user)
            return user_list
        else:
            raise ValueError("No User Found !")
