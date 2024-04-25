from model.da.da import Da
from model.entity.user import User


class UserDa(Da):
    def save(self, user):
        self.connect()
        self.cursor.execute("INSERT INTO USER_TBL(username, password, status, locked) VALUES(%s,%s,%s,%s)",
                            [user.username, user.password, user.status, user.locked])
        self.connection.commit()
        self.disconnect()

    def edit(self, user, status, locked):
        self.connect()
        self.cursor.execute("UPDATE USER_TBL SET username=%s, password=%s, status=%s, locked=%s  WHERE ID=%s",
                            [user.username, user.password, user.user_id, status, locked])
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
        if user_tuple_list:
            user_list = []
            for user_tuple in user_tuple_list:
                user = User(user_tuple[1], user_tuple[2])
                user.user_id = user_tuple[0]
                user_list.append(user)
            return user_list
        else:
            raise ValueError("No User Found !")

    def find_by_id(self, user_id):
        self.connect()
        self.cursor.execute("SELECT * FROM USER_TBL WHERE ID=%s", [user_id])
        user_tuple = self.cursor.fetchone()
        self.disconnect()
        if user_tuple:
            user = User(user_tuple[1], user_tuple[2])
            user.user_id = user_tuple[0]
            return user
        else:
            raise ValueError("No User Found !")

    def find_by_username(self, username):
        self.connect()
        self.cursor.execute("SELECT * FROM USER_TBL WHERE USERNAME=%s", [username])
        user_tuple_list = self.cursor.fetchall()
        self.disconnect()
        if user_tuple_list:
            user_list = []
            for user_tuple in user_tuple_list:
                user = User(user_tuple[1], user_tuple[2])
                user.user_id = user_tuple[0]
                user_list.append(user)
            return user_list
        else:
            raise ValueError("No User Found !")
