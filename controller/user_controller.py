from model.da.user_da import UserDa
from model.entity.user import User
from model.tools.user_validator import UserValidator


class UserController:
    def __init__(self):
        self.validator = UserValidator()

    def save(self, username, password, status, locked):
        try:
            user = User(
                self.validator.username_validator(username, "Invalid Username"),
                self.validator.password_validator(password, "Invalid Password")
            )
            user.status = status
            user.locked = locked
            user_da = UserDa()
            user_da.save(user)
            return True, f"User saved successfully\n{user}"
        except Exception as e:
            return False, str(e)

    def edit(self, user_id, username, password):
        try:
            user = User(
                self.validator.username_validator(username, "Invalid Username"),
                self.validator.password_validator(password, "Invalid Password")
            )
            user = User(username, password)
            user.user_id = user_id
            user_da = UserDa()
            old_user = user_da.find_by_id(user_id)
            user_da.edit(user)
            return True, (f"User edited successfully\nFrom : {old_user}\nTo: {user}")
        except Exception as e:
            return False, str(e)

    def remove(self, user_id):
        try:
            user_da = UserDa()
            user = user_da.find_by_id(user_id)
            user_da.remove(user_id)
            return True, f"User removed successfully\n{user}"
        except Exception as e:
            return False, str(e)

    def find_all(self):
        try:
            user_da = UserDa()
            return True, user_da.find_all()
        except Exception as e:
            return False, str(e)

    def find_by_id(self, user_id):
        try:
            user_da = UserDa()
            return True, user_da.find_by_id(user_id)
        except Exception as e:
            return False, str(e)

    def find_by_username(self, username):
        try:
            user_da = UserDa()
            return True, user_da.find_by_username(
                self.validator.username_validator(username, "Invalid Username")
            )
        except Exception as e:
            return False, str(e)
