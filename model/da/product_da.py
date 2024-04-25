from model.da.da import Da
from model.entity.product import Products


class ProductDa(Da):
    def save(self, product):
        self.connect()
        self.cursor.execute("INSERT INTO product_tbl (NAME,BRAND,SERIAL,BUY_PRICE) VALUES (%s,%s,%s,%s)",
                            [product.name, product.brand, product.serial, product.buy_price])
        self.connection.commit()
        self.disconnect()

    def edit(self, product):
        self.connect()
        self.cursor.execute("UPDATE product_tbl SET NAME=%s,BRAND=%s,SERIAL=%s,BUY_PRICE=%s WHERE ID=%s",
                            [product.name, product.brand, product.serial, product.buy_price, product.product_id])
        self.connection.commit()
        self.disconnect()

    def remove(self, product):
        self.connect()
        self.cursor.execute("DELETE FROM product_tbl WHERE ID=%s",
                            [product.product_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM product_tbl")
        products_tuple_list = self.cursor.fetchall()
        self.disconnect()
        if products_tuple_list:
            products_list = []
            for products_tuple in products_tuple_list:
                product = Products(products_tuple[1], products_tuple[2], products_tuple[3], products_tuple[4])
                product.product_id = products_tuple[0]
                products_list.append(product)
                return products_list
            else:
                raise ValueError("No products found !")

    def find_by_id(self, product_id):
        self.connect()
        self.cursor.execute("SELECT * FROM product_tbl WHERE ID=%s", [product_id])
        products_tuple = self.cursor.fetchone()
        self.disconnect()
        if products_tuple:
            product = Products(products_tuple[1], products_tuple[2], products_tuple[3], products_tuple[4])
            product.product_id = products_tuple[0]
            return product
        else:
            raise ValueError("No products found !")

    def find_by_serial(self, serial):
        self.connect()
        self.cursor.execute("SELECT * FROM product_tbl WHERE serial=%S", [serial])
        products_tuple_list = self.cursor.fetchall()
        self.disconnect()
        if products_tuple_list:
            product_list = []
        for products_tuple in products_tuple_list:
            product = Products(products_tuple[3])
            product.product_id = products_tuple[0]
            product_list.append(product)
            return product_list
        else:
            raise ValueError("no products found !")
