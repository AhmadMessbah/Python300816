from model.da.user_da import UserDa
from model.da.person_da import PersonDa
from model.entity.user import User
from model.tools.decorators import exception_handling


class UserController:
    user_da = UserDa()
    person_da = PersonDa()

    @classmethod
    @exception_handling
    def save(cls, username, password, status, locked, person_id):
        if person_id:
            person = cls.person_da.find_by_id(person_id)
            user = User(username, password)
            user.person = person
        else:
            user = User(username, password)

        user.status = status
        user.locked = locked
        cls.user_da.save(user)
        return True, f"User saved successfully {user}"

    @classmethod
    @exception_handling
    def edit(cls, user_id, username, password, status, locked, person_id):
        person = cls.person_da.find_by_id(person_id)
        user = User(username, password)
        user.person = person
        user.status = status
        user.locked = locked
        user.user_id = user_id
        old_user = cls.user_da.find_by_id(user_id)
        cls.user_da.edit(user)
        return True, (f"User edited successfully From : {old_user} To: {user}")

    @classmethod
    @exception_handling
    def remove(cls, user_id):
        user = cls.user_da.find_by_id(user_id)
        cls.user_da.remove(user_id)
        return True, f"User removed successfully {user}"

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.user_da.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, user_id):
        return True, cls.user_da.find_by_id(user_id)

    @classmethod
    @exception_handling
    def find_by_username(cls, username):
        return True, cls.user_da.find_by_username(username)

    @classmethod
    @exception_handling
    def find_by_username_and_password(cls, username, password):
        return True, cls.user_da.find_by_username_and_password(username, password)
