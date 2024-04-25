from model.entity.base import Base


class Products(Base):
    def __init__(self, name, brand, serial, buy_price):
        self.product_id = None
        self.name = name
        self.brand = brand
        self.serial = serial
        self.buy_price = buy_price
