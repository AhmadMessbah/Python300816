from model.entity.base import Base


class FinancialDoc(Base):
    def __init__(self, amount, date_time, doc_type, description):
        self.financial_doc_id = None
        self.amount = amount
        self.date_time = date_time
        self.doc_type = doc_type
        self.description = description
