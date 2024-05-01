from datetime import datetime

from model.da.financial_doc_da import Financial_Doc_Da
from model.entity.financial_doc import FinancialDoc
from model.tools.validator import Validator


class FinancialDoc_Controller:
    def __init__(self):
        self.validator = Validator()

    def save(self, amount, doc_type, description):
        try:
            financial_doc = FinancialDoc(
                self.validator.amount_validator(amount, "Invalid amount"),
                datetime.now(),
                self.validator.doc_type_validator(doc_type, "Invalid document type"),
                description
            )
            financial_doc_da = Financial_Doc_Da()
            financial_doc_da.save(financial_doc)
            return True, f"financial document saved successfully\n{financial_doc}"
        except Exception as e:
            return False, str(e)

    def edit(self, financial_doc_id, amount, doc_type):
        try:
            financial_doc = FinancialDoc(
                self.validator.amount_validator(amount, "Invalid amount"),
                datetime.now(),
                self.validator.doc_type_validator(doc_type, "Invalid document type")
            )
            financial_doc = FinancialDoc(amount, date_time, doc_type)
            financial_doc.financial_doc_id = financial_doc_id
            financial_doc_da = Financial_Doc_Da()
            old_financial_doc = financial_doc_da.find_by_id(financial_doc_id)
            financial_doc_da.edit(financial_doc)
            return True, (f"Financial Document edited successfully\nFrom : {old_financial_doc}\nTo: {financial_doc}")
        except Exception as e:
            return False, str(e)

    def remove(self, financial_doc_id):
        try:
            financial_doc_da = Financial_Doc_Da()
            financial_doc = financial_doc_da.find_by_id(financial_doc_id)
            financial_doc_da.remove(financial_doc_id)
            return True, f"Financial Document removed successfully\n{financial_doc}"
        except Exception as e:
            return False, str(e)

    def find_all(self):
        try:
            financial_doc_da = Financial_Doc_Da()
            return True, financial_doc_da.find_all()
        except Exception as e:
            return False, str(e)

    def find_by_id(self, financial_doc_id):
        try:
            financial_doc_da = Financial_Doc_Da()
            return True, financial_doc_da.find_by_id(financial_doc_id)
        except Exception as e:
            return False, str(e)

    def find_by_date(self, date_time):
        try:
            financial_doc_da = Financial_Doc_Da()
            return True, financial_doc_da.find_by_date(
                self.validator.date_time_validator(date_time, "Invalid Date")
            )
        except Exception as e:
            return False, str(e)
