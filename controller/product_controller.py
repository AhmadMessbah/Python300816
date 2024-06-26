from model.da.person_da import PersonDa
from model.da.product_da import ProductDa
from model.entity.product import Product
from model.tools.decorators import exception_handling


class ProductController:
    product_da = ProductDa()
    person_da = PersonDa()

    @classmethod
    @exception_handling
    def save(cls, name, brand, serial, buy_price, person_id):
        if person_id:
            person_id = int(person_id)
            person = cls.person_da.find_by_id(person_id)
            product = Product(name, brand, serial, buy_price, person)
        else:
            product = Product(name, brand, serial, buy_price )

        cls.product_da.save(product)
        return True, f"product saved successfully\n{product}"

    @classmethod
    @exception_handling
    def edit(cls, product_id, name, brand, serial, buy_price, person_id):
        person = cls.person_da.find_by_id(int(person_id))
        product = Product(name, brand, serial, buy_price, person)
        product.product_id = product_id
        old_product = cls.product_da.find_by_id(product_id)
        cls.product_da.edit(product)
        return True, (f"product edited successfully\nFrom : {old_product}\nTo: {product}")

    @classmethod
    @exception_handling
    def remove(cls, product_id):
        product = cls.product_da.find_by_id(product_id)
        cls.product_da.remove(product_id)
        return True, f"product removed successfully\n{product}"

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.product_da.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, product_id):
        return True, cls.product_da.find_by_id(product_id)

    @classmethod
    @exception_handling
    def find_by_person_id(cls, person_id):
        return True, cls.product_da.find_by_person_id(person_id)

    @classmethod
    @exception_handling
    def find_by_person_and_product_id(cls, person_id, product_id):
        return True, cls.product_da.find_by_person_and_product_id(person_id, product_id)

