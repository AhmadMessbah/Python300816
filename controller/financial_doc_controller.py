from datetime import datetime

from model.da.financialdocda import FinancialDocDa
from model.entity.financial_doc import FinancialDoc
from model.tools.decorators import exception_handling


class FinancialDocController:
    FinancialDocDa = FinancialDocDa()

    @classmethod
    @exception_handling
    def save(cls, amount, doc_type, description):
        financial_doc = FinancialDoc(amount, datetime.now(), doc_type, description)
        cls.FinancialDocDa.save(financial_doc)
        return True, f"financial_doc saved successfully\n{financial_doc}"

    @classmethod
    @exception_handling
    def edit(cls, financial_doc_id, amount, doc_type):
        financial_doc = FinancialDoc(amount, doc_type)
        financial_doc.financial_doc_id = financial_doc_id
        old_financial_doc = cls.FinancialDocDa.find_by_id(financial_doc_id)
        cls.FinancialDocDa.edit(financial_doc)
        return True, (f"financial_doc edited successfully\nFrom : {old_financial_doc}\nTo: {financial_doc}")

    @classmethod
    @exception_handling
    def remove(cls, financial_doc_id):
        financial_doc = cls.FinancialDocDa.find_by_id(financial_doc_id)
        cls.FinancialDocDa.remove(financial_doc_id)
        return True, f"financial_doc removed successfully\n{financial_doc}"

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.FinancialDocDa.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, financial_doc_id):
        return True, cls.FinancialDocDa.find_by_id(financial_doc_id)

    @classmethod
    @exception_handling
    def find_by_date(cls, date_time):
        return True, cls.FinancialDocDa.find_by_date(date_time)
