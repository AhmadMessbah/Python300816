from model.entity.base import Base
from model.tools.validator import Validator

class FinancialDoc(Base):
    def __init__(self, amount, date_time, doc_type, description):
        self.financial_doc_id = None
        self.amount = amount
        self.date_time = date_time
        self.doc_type = doc_type
        self.description = description
        self.person = None

    def get_amount(self):
        return self._amount

    def set_amount(self, amount):
        self._amount =  Validator.amount_validator(amount, "Invalid amount")

    def get_doc_type(self):
        return self._doc_type

    def set_doc_type(self, doc_type):
        self._doc_type =  Validator.doc_type_validator(doc_type, "Invalid document type")

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description =  description

    amount = property(get_amount, set_amount)
    doc_type = property(get_doc_type, set_doc_type)
    description = property(get_description, set_description)




