from model.da.da import Da
from model.entity.financial_doc import FinancialDoc


class Financial_Doc_Da(Da):
    def save(self, financial_doc):
        self.connect()
        self.cursor.execute("INSERT INTO FinancialDoc_tbl(AMOUNT, DATE_TIME, DOC_TYPE, DESCRIPTION) VALUES(%s,%s,%s,%s)",
                            [financial_doc.amount,financial_doc.date_time,financial_doc.doc_type, financial_doc.description])
        self.connection.commit()
        self.disconnect()

    def edit(self, financial_doc):
        self.connect()
        self.cursor.execute("UPDATE FinancialDoc_tbl SET AMOUNT=%s, DATE_TIME=%s, DOC_TYPE=%s, DESCRIPTION=%s WHERE ID=%s",
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
        financialdoc_tuple_list = self.cursor.fetchall()
        self.disconnect()
        if financialdoc_tuple_list:
            financialdoc_list = []
            for financialdoc_tuple in financialdoc_tuple_list:
                financial_doc = FinancialDoc(financialdoc_tuple[1], financialdoc_tuple[2])
                financial_doc.financial_doc_id = financialdoc_tuple[0]
                financialdoc_list.append(financial_doc)
            return financialdoc_list
        else:
            raise ValueError("No Financial Document Found !")

    def find_by_id(self, financial_doc_id):
        self.connect()
        self.cursor.execute("SELECT * FROM FinancialDoc_tbl WHERE ID=%s", [financial_doc_id])
        financialdoc_tuple = self.cursor.fetchone()
        self.disconnect()
        if financialdoc_tuple:
            financial_doc = FinancialDoc(financialdoc_tuple[1], financialdoc_tuple[2])
            financial_doc.financial_doc_id = financialdoc_tuple[0]
            return financial_doc
        else:
            raise ValueError("No Financial Document Found !")

    def find_by_date(self, date_time):
        self.connect()
        self.cursor.execute("SELECT * FROM FinancialDoc_tbl WHERE DATE_TIME=%s", [date_time])
        financialdoc_tuple_list = self.cursor.fetchall()
        self.disconnect()
        if financialdoc_tuple_list:
            financialdoc_list = []
            for financialdoc_tuple in financialdoc_tuple_list:
                financial_doc = FinancialDoc(financialdoc_tuple[1], financialdoc_tuple[2])
                financial_doc.financial_doc_id = financialdoc_tuple[0]
                financialdoc_list.append(financial_doc)
            return financialdoc_list
        else:
            raise ValueError("No Financial Document Found !")
