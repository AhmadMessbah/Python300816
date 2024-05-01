import re


class SimCard_Validator:
    def Number_Validator(self, number, message):
        if re.match(r"^[0-9]{2,11}$", number):
            return number
        else:
            raise ValueError(message)

    def Operator_Validator(self, operator, message):
        if re.match(r"^[a-zA-Z\s]{2,20}$", operator):
            return operator
        else:
            raise ValueError(message)

    def Price_Validator(self, price, message):
        if re.match(r"^[0-9]{2,11}$", price):
            return price
        else:
            raise ValueError(message)

    def Owner_Validator(self, owner, message):
        if re.match(r"^[a-zA-Z\s]{5,50}$", owner):
            return owner
        else:
            raise ValueError(message)
