from model.entity.base import Base


class SimCard(Base):
    def __init__(self, number, operator, price, owner):
        self.sim_card_id = None
        self.number = number
        self.operator = operator
        self.price = price
        self.owner = owner
