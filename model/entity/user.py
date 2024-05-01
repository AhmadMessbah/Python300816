from model.entity.user_base import UserBase


class User(UserBase):
    def __init__(self, username, password):
        self.user_id = None
        self.username = username
        self.password = password
        self.status = True
        self.locked = False
