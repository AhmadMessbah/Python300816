from model.da.da import Da
from model.da.person_da import PersonDa
from model.entity.product import Product


class ProductDa(Da):
    def save(self, product):
        self.connect()
        self.cursor.execute("INSERT INTO product_tbl (NAME,BRAND,SERIAL,BUY_PRICE,PERSON_ID) VALUES (%s,%s,%s,%s,%s)",
                            [product.name,
                             product.brand,
                             product.serial,
                             product.buy_price,
                             product.person.person_id if product.person.person_id else None])
        self.connection.commit()
        self.disconnect()

    def edit(self, product):
        if (product.name and self.find_product_count_by_person_id(product.product_id) < 3):
            self.connect()
            self.cursor.execute("UPDATE product_tbl SET NAME=%s,BRAND=%s,SERIAL=%s,BUY_PRICE=%s WHERE ID=%s",
                                [product.name,
                                 product.brand,
                                 product.serial,
                                 product.buy_price,
                                 product.person_id if product.person_id else None]
                                )
            self.connection.commit()
            self.disconnect()

    def remove(self, product_id):
        self.connect()
        self.cursor.execute("DELETE FROM product_tbl WHERE ID=%s",
                            [product_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM product_tbl")
        products_tuple_list = self.cursor.fetchall()
        self.disconnect()
        print(products_tuple_list)
        person_da = PersonDa()
        if products_tuple_list:
            product_list = []
            for product_tuple in products_tuple_list:
                product = Product(product_tuple[1],
                                  product_tuple[2],
                                  product_tuple[3],
                                  person_da.find_by_id(product_tuple[4]))
                product.product_id = product_tuple[0]
                product_list.append(product)
            return product_list
        else:
            raise ValueError("No products found !")

    def find_by_id(self, product_id):
        self.connect()
        self.cursor.execute("SELECT * FROM product_tbl WHERE ID=%s", [product_id])
        product_tuple = self.cursor.fetchone()
        self.disconnect()
        person_da = PersonDa()
        if product_tuple:
            product = Product(product_tuple[1], product_tuple[2], product_tuple[3],
                              person_da.find_by_id(product_tuple[4]))
            product.product_id = product_tuple[0]
            return product
        else:
            raise ValueError("No products found !")

    def find_by_serial(self, serial):
        self.connect()
        self.cursor.execute("SELECT * FROM product_tbl WHERE serial=%S", [serial])
        product_tuple = self.cursor.fetchone()
        self.disconnect()
        person_da = PersonDa()
        if product_tuple:
            product = Product(product_tuple[1], product_tuple[2], product_tuple[3],
                              person_da.find_by_id(product_tuple[4]))
            product.product_id = product_tuple[0]
            return product
        else:
            raise ValueError("No Products Found !")

    def find_product_count_by_person_id(self, person_id):
        self.connect()
        self.cursor.execute("SELECT * FROM PRODUCT_COUNT WHERE PERSON_ID=%s", [person_id])
        product_count = self.cursor.fetchone()
        self.disconnect()
        if product_count:
            return int(product_count[1])
        else:
            return 0
