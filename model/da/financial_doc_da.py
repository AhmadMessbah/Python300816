from model.da.da import Da
from model.entity.financial_doc import FinancialDoc
from model.da.person_da import PersonDa


class FinancialDocDa(Da):
    def save(self, financial_doc):
        self.connect()
        self.cursor.execute(
            "INSERT INTO FinancialDoc_tbl(AMOUNT, DATE_TIME, DOC_TYPE, DESCRIPTION, PERSON_ID) VALUES(%s,%s,%s,%s,%s)",
            [financial_doc.amount, financial_doc.date_time, financial_doc.doc_type, financial_doc.description,
             financial_doc.person.person_id])
        self.connection.commit()
        self.disconnect()

    def edit(self, financial_doc):
        self.connect()
        self.cursor.execute(
            "UPDATE FinancialDoc_tbl SET AMOUNT=%s, DATE_TIME=%s, DOC_TYPE=%s, DESCRIPTION=%s WHERE ID=%s",
            [financial_doc.amount, financial_doc.date_time, financial_doc.doc_type,
             financial_doc.description, financial_doc.financial_doc_id])
        self.connection.commit()
        self.disconnect()

    def remove(self, financial_doc_id):
        self.connect()
        self.cursor.execute("DELETE FROM FinancialDoc_tbl WHERE ID=%s",
                            [financial_doc_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM FinancialDoc_tbl")
        financial_tuple_list = self.cursor.fetchall()
        self.disconnect()
        person_da = PersonDa()
        if financial_tuple_list:
            financial_list = []
            for financial_tuple in financial_tuple_list:
                financial_doc = FinancialDoc(financial_tuple[1], financial_tuple[2], financial_tuple[3],
                                             financial_tuple[4])
                financial_doc.financial_doc_id = financial_tuple[0]
                financial_doc.person = person_da.find_by_id(financial_tuple[5])
                financial_list.append(financial_doc)
            return financial_list
        else:
            raise ValueError("No Financial Document Found !")

    def find_by_id(self, financial_doc_id):
        self.connect()
        self.cursor.execute("SELECT * FROM FinancialDoc_tbl WHERE ID=%s", [financial_doc_id])
        financial_tuple = self.cursor.fetchone()
        self.disconnect()
        person_da = PersonDa()
        if financial_tuple:
            financial_doc = FinancialDoc(financial_tuple[1], financial_tuple[2],financial_tuple[3], financial_tuple[4])
            financial_doc.financial_doc_id = financial_tuple[0]
            financial_doc.person = person_da.find_by_id(financial_tuple[5])
            return financial_doc
        else:
            raise ValueError("No Financial Document Found !")

    def find_by_date(self, date_time):
        self.connect()
        self.cursor.execute("SELECT * FROM FinancialDoc_tbl WHERE DATE_TIME=%s", [date_time])
        financial_tuple_list = self.cursor.fetchall()
        self.disconnect()
        person_da = PersonDa()
        if financial_tuple_list:
            financial_list = []
            for financial_tuple in financial_tuple_list:
                financial_doc = FinancialDoc(financial_tuple[1], financial_tuple[2], financial_tuple[3],
                                             financial_tuple[4])
                financial_doc.financial_doc_id = financial_tuple[0]
                financial_doc.person = person_da.find_by_id(financial_tuple[5])
                financial_list.append(financial_doc)
            return financial_list
        else:
            raise ValueError("No Financial Document Found !")

    def find_by_person_id(self, person_id):
        self.connect()
        self.cursor.execute("SELECT * FROM FinancialDoc_tbl WHERE ID=%s", [person_id])
        financial_tuple_list = self.cursor.fetchall()
        self.disconnect()
        person_da = PersonDa()
        if financial_tuple_list:
            financial_list = []
            for financial_tuple in financial_tuple_list:
                financial_doc = FinancialDoc(financial_tuple[1], financial_tuple[2], financial_tuple[3],
                                             financial_tuple[4])
                financial_doc.financial_doc_id = financial_tuple[0]
                financial_doc.person = person_da.find_by_id(financial_tuple[5])
                financial_list.append(financial_doc)
            return financial_list
        else:
            raise ValueError("No Financial Document Found !")