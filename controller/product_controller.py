from model.da.product_da import ProductDa
from model.entity.product import Product
from model.tools.validator import Validator


class ProductController:
    def __init__(self):
        self.validator = Validator()

    def save(self, name, brand, serial, buy_price):
        try:
            product = Product(
                self.validator.name_validator(name, "Invalid Name"),
                self.validator.name_validator(brand, "Invalid Brand"),
                self.validator.name_validator(serial, "Invalid Serial"),
                self.validator.name_validator(buy_price, "Invalid Price")

            )
            product_da = ProductDa()
            product_da.save(product)
            return True, f"Product saved successfully\n{product}"

        except Exception as e:
            return False, str(e)

    def edit(self, product_id, name, brand, serial, buy_price):
        try:
            product = Product(
                self.validator.name_validator(name, "Invalid Name"),
                self.validator.name_validator(brand, "Invalid Brand"),
                self.validator.name_validator(serial, "Invalid Serial"),
                self.validator.name_validator(buy_price, "Invalid Price")
            )
            product = Product(name, brand, serial, buy_price)
            product.product_id = product_id
            product_da = ProductDa()
            old_product = product_da.find_by_id(product_id)
            product_da.edit(product)
            return True, (f"Product edited successfully\nFrom : {old_product}\nTo: {product}")
        except Exception as e:
            return False, str(e)

    def remove(self, product_id):
        try:
            product_da = ProductDa()
            product = product_da.find_by_id(product_id)
            product_da.remove(product_id)
            return True, f"Product removed successfully\n{product}"
        except Exception as e:
            return False, str(e)

    def find_all(self):
        try:
            product_da = ProductDa()
            return True, product_da.find_all()
        except Exception as e:
            return False, str(e)

    def find_by_id(self, product_id):
        try:
            product_da = ProductDa()
            return True, product_da.find_by_id(product_id)
        except Exception as e:
            return False, str(e)
