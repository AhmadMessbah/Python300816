from model.da.sim_card_da import SimCardDa
from model.entity.sim_card import SimCard
from model.tools.validator import Validator


class SimCardController:
    def __init__(self):
        self.validator = Validator()

    def save(self, number, operator, price, owner):
        try:
            sim_card = SimCard(
                self.validator.sim_card_validator(number, "Invalid Number"),
                self.validator.sim_card_validator(operator, "Invalid Name"),
                self.validator.sim_card_validator(price, "Invalid Value"),
                self.validator.sim_card_validator(owner, "Invalid Input")
            )
            sim_card_da = SimCardDa()
            sim_card_da.save(sim_card)
            return True, f"SimCard saved successfully\n{sim_card}"
        except Exception as e:
            return False, str(e)

    def edit(self, sim_card_id, number, operator, price, owner):
        try:
            sim_card = SimCard(
                self.validator.sim_card_validator(number, "Invalid Number"),
                self.validator.sim_card_validator(operator, "Invalid Name"),
                self.validator.sim_card_validator(price, "Invalid Value"),
                self.validator.sim_card_validator(owner, "Invalid Input")
            )
            sim_card = sim_card(number, operator, price, owner)
            sim_card.sim_card_id = sim_card_id
            sim_card_da = SimCardDa()
            old_sim_card = sim_card_da.find_by_id(sim_card_id)
            sim_card_da.edit(sim_card)
            return True, (f"SimCard edited successfully\nFrom : {old_sim_card}\nTo: {sim_card}")
        except Exception as e:
            return False, str(e)

    def remove(self, sim_card_id):
        try:
            sim_card_da = SimCardDa()
            sim_card = sim_card_da.find_by_id(sim_card_id)
            sim_card_da.remove(sim_card_id)
            return True, f"sim_card removed successfully\n{sim_card}"
        except Exception as e:
            return False, str(e)

    def find_all(self):
        try:
            sim_card_da = SimCardDa()
            return True, sim_card_da.find_all()
        except Exception as e:
            return False, str(e)

    def find_by_id(self, sim_card_id):
        try:
            sim_card_da = SimCardDa()
            return True, sim_card_da.find_by_id(sim_card_id)
        except Exception as e:
            return False, str(e)

    def find_by_owner(self, owner):
        try:
            sim_card_da = SimCardDa()
            return True, sim_card_da.find_by_owner(
                self.validator.sim_card_validator(owner, "Invalid Owner")
            )
        except Exception as e:
            return False, str(e)
