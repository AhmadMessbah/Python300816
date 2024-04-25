import mysql.connector


class product_da:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connect = (mysql.connector.connect
            (
            host="localhost",
            user="root",
            password="mft123",
            database="mft1"
            ))
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()
