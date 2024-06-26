from model.da.sim_card_da import SimCardDa
from model.da.person_da import PersonDa
from model.entity.sim_card import SimCard
from model.tools.decorators import exception_handling


class SimCardController:
    sim_card_da = SimCardDa()
    person_da = PersonDa()

    @classmethod
    @exception_handling
    def save(cls, number, operator, price, owner_id):
        price = int(price)
        if owner_id:
            owner = cls.person_da.find_by_id(owner_id)
            sim_card = SimCard(number, operator, price, owner)
        else:
            sim_card = SimCard(number, operator, price)

        cls.sim_card_da.save(sim_card)
        return True, f"SimCard saved successfully\n{sim_card}"

    @classmethod
    @exception_handling
    def edit(cls, sim_card_id, number, operator, price, owner_id):
        price = int(price)
        owner = cls.person_da.find_by_id(owner_id)
        sim_card = SimCard(number, operator, price, owner)
        sim_card.sim_card_id = sim_card_id
        old_sim_card = cls.sim_card_da.find_by_id(sim_card_id)
        cls.sim_card_da.edit(sim_card)
        return True, (f"SimCard edited successfully\nFrom : {old_sim_card}\nTo: {sim_card}")

    @classmethod
    @exception_handling
    def remove(cls, sim_card_id):
        sim_card_id= int(sim_card_id)
        sim_card = cls.sim_card_da.find_by_id(sim_card_id)
        cls.sim_card_da.remove(sim_card_id)
        return True, f"sim_card removed successfully\n{sim_card}"

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.sim_card_da.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, sim_card_id):
        return True, cls.sim_card_da.find_by_id(sim_card_id)

    @classmethod
    @exception_handling
    def find_by_owner_id(cls, owner_id):
        return True, cls.sim_card_da.find_by_owner_id(owner_id)
