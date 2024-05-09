from model.entity.base import Base
from model.tools.validator import Validator


class User(Base):
    def __init__(self, username, password):
        self.user_id = None
        self.username = username
        self.password = password
        self.status = True
        self.locked = False

    def get_username(self):
        return self._username

    def set_username(self, username):
        self._username = Validator.username_validator(username, "Invalid Username")

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = Validator.password_validator(password, "Invalid Password")

    username = property(get_username, set_username)
    password = property(get_password, set_password)
