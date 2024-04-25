import re


class Validator:
    def name_validator(self, name, message):
        if re.match("^[a-zA-Z\s]{2,30}$", name):
            return name
        else:
            raise ValueError(message)


