import re


class Validator:
    def name_validator(self, name, message):
        if re.match(r"^[a-zA-Z\s]{2,30}$", name):
            return name
        else:
            raise ValueError(message)


