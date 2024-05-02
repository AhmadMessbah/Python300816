from datetime import datetime

from model.da.financial_doc_da import Financial_Doc_Da
from model.entity.financial_doc import FinancialDoc
from model.tools.decorators import exception_handling


class FinancialDoc_Controller:
    financial_doc_da = Financial_Doc_Da

    @classmethod
    @exception_handling
    def save(cls, amount, doc_type, description):
        financial_doc = FinancialDoc(amount,doc_type,description)
        cls.financial_doc_da.save(financial_doc)
        return True, f"financial_doc saved successfully\n{financial_doc}"

    @classmethod
    @exception_handling
    def edit(cls, financial_doc_id, amount, doc_type):
        financial_doc = FinancialDoc(amount, doc_type)
        financial_doc.financial_doc_id = financial_doc_id
        old_financial_doc = cls.financial_doc_da.find_by_id(financial_doc_id)
        cls.financial_doc_da.edit(financial_doc)
        return True, (f"financial_doc edited successfully\nFrom : {old_financial_doc}\nTo: {financial_doc}")

    @classmethod
    @exception_handling
    def remove(cls, financial_doc_id):
        financial_doc = cls.Financial_Doc_Da.find_by_id(financial_doc_id)
        cls.Financial_Doc_Da.remove(financial_doc_id)
        return True, f"financial_doc removed successfully\n{financial_doc}"

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.financial_doc_da.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, financial_doc_id):
        return True, cls.financial_doc_da.find_by_id(financial_doc_id)



    @classmethod
    @exception_handling
    def find_by_date(cls, date_time):
        return True, cls.financial_doc_da.find_by_date(date_time)