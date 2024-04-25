import re


class UserValidator:
    def username_validator(self, username, message):
        if re.match(r"^[a-zA-Z\s]{2,30}$", username):
            return username
        else:
            raise ValueError(message)


    def password_validator(self, password, message):
        if re.match(r"^[a-zA-Z0-9@!#$%^&*\s]{8,16}$", password):
            return password
        else:
            raise ValueError(message)


